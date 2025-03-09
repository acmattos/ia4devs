import torch
from unsloth import FastLanguageModel
from transformers import TextStreamer

###############################################################################
# Configuração para o Unsloth
###############################################################################
# Tamanho máximo da sequência de entrada
max_seq_length = 2048           # Máximo de tokens que o modelo pode processar de uma vez
# Tipo de dados para os pesos do modelo
dtype          = torch.bfloat16 # Formato de precisão reduzida para economia de memória
                                # bfloat16 é bom para treinar em GPUs modernas
# Habilita quantização em 4 bits
load_in_4bit   = True           # Reduz uso de memória mantendo boa performance


alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

# 1. Primeiro carrega o modelo base
#base_model = "unsloth/llama-3-8b-bnb-4bit"  # Modelo base do LLaMA-3
base_model = "./lora_model_llama-3-8b-bnb-4bit"

from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
model = AutoPeftModelForCausalLM.from_pretrained(
    base_model, # YOUR MODEL YOU USED FOR TRAINING
    load_in_4bit = load_in_4bit,
)
tokenizer = AutoTokenizer.from_pretrained(base_model)


# model, tokenizer = FastLanguageModel.from_pretrained(
#     model_name = base_model, # YOUR MODEL YOU USED FOR TRAINING
#     max_seq_length = max_seq_length,
#     dtype = dtype,
#     load_in_4bit = load_in_4bit,
# )

# # 3. Carrega os pesos do LoRA
# #model.load_adapter("./lora_model_llama-3-8b-bnb-4bit")

# # Prepara o modelo para inferência
# FastLanguageModel.for_inference(model)
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

# Configura streaming
text_streamer = TextStreamer(tokenizer, skip_prompt=True)

# Gera resposta
outputs = model.generate(
    **inputs,
    streamer = text_streamer,
    max_new_tokens = 128,
    temperature = 0.9,
    do_sample = True
)
# Decodifica os tokens em texto
responses = tokenizer.batch_decode(outputs)
print("\nResposta do modelo:")
print(responses[0])