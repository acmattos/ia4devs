import json
import sys
import torch
import triton
import transformers
from datasets import load_dataset
from tqdm import tqdm
from transformers import TrainingArguments, TextStreamer
from trl import SFTTrainer
from unsloth import FastLanguageModel, is_bfloat16_supported

###############################################################################
# Detalhes do Ambiente de Execução do Modelo
###############################################################################
print()
print("###############################################################################")
print("# Informações do Ambiente de Execução...")
gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)

print(f"\nVersão do Python      : {sys.version}")
print(f"Versão do PyTorch     : {torch.__version__}")
print(f"Versão do Triton      : {triton.__version__}")
print(f"Versão do Transformers: {transformers.__version__}")
print(f"CUDA disponível       : {torch.cuda.is_available()}")
print(f"Versão do CUDA        : {torch.version.cuda}")
print(f"Versão do cuDNN       : {torch.backends.cudnn.version()}")
print(f"Números de GPUs       : {torch.cuda.device_count()}")
print(f"Nome da GPU 0         : {gpu_stats.name}")
print(f"Memória Máxima        : {max_memory} GB")
print(f"Memória reservada     : {start_gpu_memory} GB")
print()

###############################################################################
# Configuração para o Unsloth
###############################################################################
torch_dtype = torch.bfloat16 # Formato de precisão reduzida para economia de memória
                             # bfloat16 é bom para treinar em GPUs modernas
# Condicional para verificar a compatibilidade com bfloat16
if not is_bfloat16_supported():
    print("Aviso: bfloat16 não é suportado, usando fp16.")
    torch_dtype = torch.float16  # Ajusta para fp16 se bfloat16 não for suportado

# unsloth_config = {
# Tamanho máximo da sequência de entrada
max_seq_length = 2048         # Máximo de tokens que o modelo pode processar de uma vez
# Tipo de dados para os pesos do modelo
dtype          = torch_dtype  # Formato de precisão reduzida para economia de memória
                                # bfloat16 é bom para treinar em GPUs modernas
# Habilita quantização em 4 bits
load_in_4bit   = True          # Reduz uso de memória mantendo boa performance
# Lista de modelos pré-treinados otimizados para 4 bits
fourbit_models = [
    # Modelos Mistral (7B parâmetros)
    "unsloth/mistral-7b-v0.3-bnb-4bit",          # Modelo base
    "unsloth/mistral-7b-instruct-v0.3-bnb-4bit", # Versão para instruções    
    # Modelos LLaMA-3
    "unsloth/llama-3-8b-bnb-4bit",               # 8B parâmetros
    "unsloth/llama-3-8b-Instruct-bnb-4bit",      # Versão instrução
    "unsloth/llama-3-70b-bnb-4bit",              # 70B parâmetros    
    # Modelos Phi (menores e mais rápidos)
    "unsloth/Phi-3-mini-4k-instruct",            # Versão mini
    "unsloth/Phi-3-medium-4k-instruct",          # Versão média    
    # Outros modelos
    "unsloth/mistral-7b-bnb-4bit",              # Mistral alternativo
    "unsloth/gemma-7b-bnb-4bit",                # Modelo Gemma do Google
]
chosen_model   = fourbit_models[2]
lora_model     = "lora_model_" + chosen_model.split("/")[-1]
# }

###############################################################################
# Carregamento e Configuração para o Unsloth
###############################################################################
print("###############################################################################")
print(f"# Carregando o modelo e tokenizador para: {chosen_model}...")
print()
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name          = chosen_model,        # Usa LLaMA-3 8B (índice 2 da lista)
    max_seq_length      = max_seq_length,      # Tamanho máximo da sequência (2048)
    dtype               = dtype,               # Tipo de dados (bfloat16)
    load_in_4bit        = load_in_4bit,        # Quantização em 4 bits
    attn_implementation = "flash_attention_2", # Usa Flash Attention 2
    device_map          = "auto",              # Otimiza distribuição na GPU
)
print()
print(f"Modelo {chosen_model} e tokenizador carregados e com sucesso!")
print()

print("###############################################################################")
print("Configurando o modelo para fine-tuning com LoRA (Low Rank Adaptation)...")
print()
model = FastLanguageModel.get_peft_model(
    # Aplica LoRA para fine-tuning eficiente
    model,                                  # Modelo base carregado
    r                          = 16,        # Rank da matriz LoRA
    # Camadas que serão adaptadas
    target_modules             = [
        "q_proj",                           # Query projection
        "k_proj",                           # Key projection
        "v_proj",                           # Value projection
        "o_proj",                           # Output projection
        "gate_proj",                        # Gate projection
        "up_proj",                          # Upscaling projection
        "down_proj",                        # Downscaling projection
    ],
    # Configura parâmetros de treinamento
    lora_alpha                 = 16,        # Escala de adaptação
    lora_dropout               = 0,         # Sem dropout
    bias                       = "none",    # Não treina bias
    # Otimiza uso de memória
    use_gradient_checkpointing = "unsloth", # Economia de memória
    random_state               = 3407,      # Semente aleatória
    use_rslora                 = False,     # Sem RS-LoRA
    loftq_config               = None,      # Sem LoftQ
)

# Se o modelo suportar gradient_checkpointing, habilite para salvar memória
if hasattr(model, 'gradient_checkpointing_enable'):
    model.gradient_checkpointing_enable()
    
print()
print(f"Modelo configurado o modelo para fine-tuning com LoRA (Low Rank Adaptation)")
print()

###############################################################################
# Configurando e Carregando Os Dados para o Unsloth
###############################################################################
print("###############################################################################")
print("# Configurando e Carregando Os Dados para o Unsloth...")
print()

processed_file = "trn_processed.json"
dataset_file   = "trn_processed_dataset.json"

def create_alpaca_prompt():
    return """
    Below is an instruction that describes a task, paired with an input that 
    provides further context. Write a response that appropriately completes 
    the request.

    ### Instruction:
    {}

    ### Input:
    {}

    ### Response:
    {}
    """

alpaca_prompt = create_alpaca_prompt()

def count_records(file):
   total_lines = sum(1 for line in open(file, 'r', encoding='utf-8'))
   return total_lines

def create_train_dataset(processed_file, total_lines):
    processed_dataset = []
    with open(processed_file, 'r', encoding='utf-8') as file:
        for line in tqdm(file, total=total_lines, desc="Processando linhas"):
            # Remove espaços em branco e quebras de linha
            line = line.strip()
            if not line or line == "[" or line == "]":  # Pula linhas vazias, [, ]
                continue
            # Remove vírgula no final da linha se existir
            if line.endswith(','):
                line = line[:-1]

            # Converte a linha em objeto JSON
            item = json.loads(line)
            
            # Extrai e limpa os campos
            product = str(item.get('product', '')).strip()
            description = str(item.get('description', '')).strip()
            
            # Só adiciona se ambos os campos não estiverem vazios
            if product and description:
                processed_dataset.append({
                    'instruction': "GET THE DESCRIPTION OF THIS PRODUCT",
                    'input': product,
                    'output': description
                })
    return processed_dataset


def format_dataset_into_model_input(processed_dataset):
    # Inicializando as listas para armazenar os dados
    instructions = []
    inputs = []
    outputs = []
    # Salvar o novo arquivo dataset
    with open(dataset_file, 'w') as output_file:
        for item in tqdm(processed_dataset, desc="Salvando registros"):
            # Cria o registro no formato esperado
            instructions.append("GET THE DESCRIPTION OF THIS PRODUCT")
            inputs.append(item["input"])
            outputs.append(item["output"])
    
        # Criando o dicionário final
        formatted_data = {
            "instruction": instructions,
            "input": inputs,
            "output": outputs
        }        
        # Salva uma linha por registro
        json.dump(formatted_data, output_file, indent = 1)
    print(f"\nDataset salvo em                             : {dataset_file}")        


def formatting_prompts_func(examples):
    texts = []
    for i in range(len(examples['instruction'])):
        text = alpaca_prompt.format(
            examples['instruction'][i], 
            examples['input'][i], 
            examples['output'][i]) + tokenizer.eos_token
        texts.append(text)
    return { "text" : texts }

print("###############################################################################")
print("# Criando o Conjunto de Dados para Treinamento do Modelo...")
print()
# Conta linhas do arquivo
total_lines = count_records(processed_file)
train_dataset = create_train_dataset(processed_file, total_lines)

print()
print("###############################################################################")
print("# Gerando o Arquivo com o Conjunto de Dados para Treinamento do Modelo...")
print()
format_dataset_into_model_input(train_dataset)

print()
print("###############################################################################")
print("# Gerando o Dataset para Treinamento do Modelo...")
print()
dataset = load_dataset("json", data_files=dataset_file, split = "train")
print("\nDataset geardo com sucesso:", dataset)

print()
print("###############################################################################")
print("# Convertendo o Dataset para Treinamento do Modelo em Prompts...")
print()
dataset = dataset.map(
    formatting_prompts_func,          # Função que será aplicada a cada batch
    batched    = True,                # Processa em batches para maior eficiência
    batch_size = 1024,                # Define tamanho do batch
    num_proc   = 1,                   # Nnúmero de processos para paralelização
    desc       = "Formatando prompts" # Descrição para a barra de progresso
)
print("Dataset convertido com sucesso:", dataset)
print(dataset.column_names)

print()
print("###############################################################################")
print("# Configurando o Treinador SFT (Supervised Fine-Tuning)...")
print()
trainingArguments = TrainingArguments(
    # Tamanho dos batches e gradientes
    per_device_train_batch_size = 2,            # Exemplos por batch na GPU
    gradient_accumulation_steps = 4,            # Acumula gradientes antes de atualizar    
    # Etapas de treinamento
    warmup_steps                = 5,            # Passos de aquecimento
    max_steps                   = 1,           # Total de passos de treinamento
    #num_train_epochs            = 1,
    # Taxa de aprendizado e otimização
    learning_rate               = 2e-4,         # Taxa de aprendizado
    weight_decay                = 0.01,         # Regularização L2
    lr_scheduler_type           = "linear",     # Decaimento linear da taxa
    # Precisão e performance
    fp16 = not is_bfloat16_supported(),         # Usa FP16 se bfloat16 não disponível
    bf16 = is_bfloat16_supported(),             # Usa bfloat16 se disponível  
    gradient_checkpointing      = True,         # Ativa gradient checkpointing
    optim                       = "adamw_8bit", # Otimizador em 8 bits  
    max_grad_norm               = 0.3,          # Limita gradientes
    # Logging e saída
    logging_steps               = 1,            # Frequência de log
    output_dir                  = "outputs",    # Diretório de saída
    save_steps                  = 1000,         # Frequência de salvamento do modelo
    # Reprodutibilidade
    seed                        = 3407,         # Semente aleatória
)

trainer = SFTTrainer(
    # Configurações básicas
    model              = model,          # Modelo LoRA configurado
    tokenizer          = tokenizer,      # Tokenizador do modelo
    train_dataset      = dataset,        # Dataset formatado
    dataset_text_field = "text",         # Campo que contém o texto
    max_seq_length     = max_seq_length, # Tamanho máximo da sequência
    dataset_num_proc   = 1,              # Número de processos para processamento
    packing            = False,          # Desativa empacotamento de sequências
    # Argumentos de treinamento
    args = trainingArguments,
)
print()
print("Treinador SFT configurado com sucesso!")

print()
print("###############################################################################")
print("# Iniciando o Treinamento do Modelo...")
print()
trainer_stats = trainer.train()

print()
# Análise das estatísticas de treinamento
print("Estatísticas do Treinamento")
print(f"Tempo total de treinamento       : {trainer_stats.metrics['train_runtime']:.2f} segundos ({round(trainer_stats.metrics['train_runtime']/60, 2)} min)")
print(f"Velocidade de processamento      : {trainer_stats.metrics['train_samples_per_second']:.2f} samples/s")
print(f"Loss final do treinamento        : {trainer_stats.metrics['train_loss']:.4f}")
# Estatísticas de memória
used_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
used_memory_for_lora = round(used_memory - start_gpu_memory, 3)
used_percentage = round(used_memory / max_memory * 100, 3)
lora_percentage = round(used_memory_for_lora / max_memory * 100, 3)
print(f"\nEstatísticas de Memória GPU")
print(f"Pico de memória reservada        : {used_memory:.3f} GB")
print(f"Pico de memória para treinamento : {used_memory_for_lora:.3f} GB")
print(f"Percentual da memória máxima     : {used_percentage:.3f}%")
print(f"Percentual usado no treinamento  : {lora_percentage:.3f}%")
if used_percentage > 100:
    print("\nAVISO: O uso de memória ultrapassou o limite máximo recomendado!")
print("\nTreinamento concluido com sucesso!")

print()
print("###############################################################################")
print("# Preparando o modelo para fazer inferência (previsões)...")
print()
# Prepara o modelo para inferência
FastLanguageModel.for_inference(model)
# Tokeniza e move para GPU
inputs = tokenizer(
     # Lista com os prompts
    [  
        # Formata o prompt usando template Alpaca
        alpaca_prompt.format(
            "GET THE DESCRIPTION OF THIS PRODUCT", # Instrução
            "Girls Ballet Tutu Neon Blue",         # Produto
            "",                                    # Resposta vazia
        )
    ],
    return_tensors = "pt"  # Retorna tensores PyTorch 
).to("cuda")               # Move para GPU

# Gera resposta
outputs = model.generate(
    **inputs,
    max_new_tokens = 128,  # Máximo de tokens na resposta
    temperature    = 0.2,  # Controla aleatoriedade (0.0 a 1.0)
    do_sample      = True, # Usa amostragem probabilística
    use_cache      = True  # Ativa o cache para melhorar a velocidade de geração
)

# Decodifica os tokens em texto
responses = tokenizer.batch_decode(outputs)
print("\nResposta do modelo:")
print(responses[0])
print()

print("###############################################################################")
print("# Configurando e executando a geração de texto com streaming...")
print()
# Prepara o modelo para inferência
FastLanguageModel.for_inference(model)
# Prepara o input usando o template Alpaca
inputs = tokenizer(
    [  # Lista com os prompts
        alpaca_prompt.format(
            "GET THE DESCRIPTION OF THIS PRODUCT",  # Instrução
            "Girls Ballet Tutu Neon Blue",         # Produto
            "",                                    # Resposta vazia
        )
    ],
    return_tensors = "pt"   # Retorna tensores PyTorch
).to("cuda")               # Move para GPU

# Configuração mais detalhada
text_streamer = TextStreamer(
    tokenizer,
    skip_prompt         = True, # Não mostra o prompt
    skip_special_tokens = True  # Não mostra tokens especiais
)

# Geração com mais parâmetros
outputs = model.generate(
    **inputs,
    streamer       = text_streamer,
    max_new_tokens = 128,  # Máximo de tokens na resposta
    temperature    = 0.2,  # Controla aleatoriedade (0.0 a 1.0)
    do_sample      = True, # Usa amostragem probabilística
    top_p          = 0.95, # Nucleus sampling
    use_cache      = True, # Ativa o cache para melhorar a velocidade de geração
)

print()
print("###############################################################################")
print("# Salvando o Modelo Treinado...")
print()
# model.save_pretrained(lora_model) #This ONLY saves the LoRA adapters, and not the full model.
# tokenizer.save_pretrained(lora_model)
# model.save_pretrained_merged(
#     lora_model,                   # Diretório onde o modelo será salvo
#     tokenizer,                    # Tokenizer usado com o modelo
#     save_method = "merged_16bit", # Método de salvamento em precisão de 16 bits
# )
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM DO TREINAMENTO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
