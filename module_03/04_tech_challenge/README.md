# Preparação do Ambiente

0 - https://developer.nvidia.com/cuda-12-6-3-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local
1 - https://github.com/woct0rdho/triton-windows
2 - https://pytorch.org/get-started/locally/
3 - https://docs.unsloth.ai/get-started/installing-+-updating/windows-installation
OBS:   pip install unsloth==2025.1.5
       pip install --no-deps "unsloth>=2025.3.8" "unsloth_zoo>=2025.3.7" --upgrade --force-reinstall

##################
RAG:

pip install huggingface_hub
pip install langchain langchain-community chromadb

# Processamento dos Dados
process_data.py

The AmazonTitles-1.3MM".(https://drive.google.com/file/d/12zH4mL2RX8iSvH0VCNnd3QxO4DzuHWnK/view?usp=sharing)

2248619
trn.json

{"uid": "0001360000", "title": "Mog's Kittens", "content": "Judith Kerr&#8217;s best&#8211;selling adventures of that endearing (and exasperating) cat Mog have entertained children for more than 30 years. Now, even infants and toddlers can enjoy meeting this loveable feline. These sturdy little board books&#8212;with their bright, simple pictures, easy text, and hand&#8211;friendly formats&#8212;are just the thing to delight the very young. Ages 6 months&#8211;2 years.", "target_ind": [146, 147, 148, 149, 495], "target_rel": [1.0, 1.0, 1.0, 1.0, 1.0]}
{"uid": "0000031895", "title": "Girls Ballet Tutu Neon Blue", "content": "Dance tutu for girls ages 2-8 years. Perfect for dance practice, recitals and performances, costumes or just for fun!", "target_ind": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 31, 33, 42, 46, 54, 58, 111, 113, 125, 126, 159, 163, 202, 203, 204, 205, 206, 207], "target_rel": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}

utilizar title e content
remover title e content vazios, bem como content com conteudo menor do que 100 caracteres
1216560
trn_processed.json
[
 {"product": "Mogs Kittens", "description": "Judith Kerr8217s best8211selling adventures of that endearing and exasperating cat Mog have entertained children for more than 30 years Now even infants and toddlers can enjoy meeting this loveable feline These sturdy little board books8212with their bright simple pictures easy text and hand8211friendly formats8212are just the thing to delight the very young Ages 6 months82112 years"},
 {"product": "Girls Ballet Tutu Neon Blue", "description": "Dance tutu for girls ages 28 years Perfect for dance practice recitals and performances costumes or just for fun"},
]

## Execução 

> python .\process_data.py

Lendo os registros do arquivo              : 100%|███████████████████████████████████| 2248619/2248619 [00:35<00:00, 62903.00it/s]
Processando registros lidos                : 100%|███████████████████████████████████| 2248619/2248619 [00:14<00:00, 155615.25it/s]
Salvando registros processado em arquivo   : 100%|███████████████████████████████████| 1216560/1216560 [00:10<00:00, 117362.03it/s] 
Total de registros no arquivo original     : 2,248,619
Total de registros processados (não vazios): 1,216,560
Arquivo processado salvo em                : trn_processed.json

# Fine-Tuning

O processo de fine-tuning do modelo envolve duas etapas: na primenira, 
realizamos o fine-tuning do modelo escolhido ("unsloth/llama-3-8b-bnb-4bit") 
enquanto na segunda, interrogamos o modelo treinado 
(./lora_model_llama-3-8b-bnb-4bit).

## Treinamento do Modelo

Nosso código para o treinamento do modelo está disponível no arquivo 
"fine_tuning.py".

O proceso de fine-tuning é feito a partir do arquivo processado 
(trn_processed.json) na fase de preparação dos dados para treinamento.

Inicialmente, a configuração do Unsloth é feita, de forma a preparar o modelo 
para fine-tuning. Com a configuração pronta, modelo e tokenizador são carregados
e retornado. Depois, aplicamos os adaptadores LoRA ao mesmo modelo, Deixando-o 
pronto para o treinamento.

Neste momento, iniciamos a preparação dos dados que serão utilizados para o 
finetunig do modelo. Ele é preparado de forma a agrupar os produtos como 
grupo de entrada (input) e as descrições como grupo de saída (output). As 
instruções (perguntas que serão feitas ao modelo) ficam no grupo de 
instruções (instructions). Esta preparação é salva em arquivo 
(trn_processed_dataset.json) para ser utilizada mais adiante.

Após ser carregado como um dataset, é transformado em um "prompt dataset"
para ser passado para o treinador do modelo. Então, o trainamento pe realizado.
Neste momento, uma mudançao de foco precisou ser feita: a quantidade de itens 
a serem treinadas (1.216.560) implicava em um tempo de treinamento que excediam 
7 dias. Com isto, o "prompt dataset" foi reduzido para 5000 item, o que permitiu
a aplicação de duas épocas de treinamento (algo em torno de 1250 iterações) tomando
um total 2:30 para que a tarefa fosse realizada. É importante ressaltar que a 
configuração presente no código, a GPU utilizada e o conjunto de dados de treino
influenciam diretamente no tempo de execução do treinamento. Algumas estatísticas 
são mostradas após o treino (tempo gasto, consumo de memória).

Ao finalizarmos esta etapa, preparamos o modelo treinado para a realização de 
inferências. Duas consultas são realizadas, apenas para mostrar as capacidades 
de exibição das respostas às consultas: a exibição completa, após o resultado 
retornado ou sua apresentação conforme o modelo vai gerando a resposta.

Consluído este pequeno teste, salvamos o modelo e seus adaptadores LoRA em localmente.

A seguir, o log de execução deste código:

'''
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge> python .\fine_tuning.py
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
🦥 Unsloth Zoo will now patch everything to make training faster!

###############################################################################
# Informações do Ambiente de Execução
###############################################################################

Versão do Python      : 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)]
Versão do PyTorch     : 2.6.0+cu126
Versão do Triton      : 3.2.0
Versão do Transformers: 4.49.0
CUDA disponível       : True
Versão do CUDA        : 12.6
Versão do cuDNN       : 90501
Números de GPUs       : 1
Nome da GPU 0         : NVIDIA GeForce RTX 4060 Laptop GPU
Memória Máxima        : 7.996 GB
Memória reservada     : 0.0 GB

###############################################################################
# Criando Configurações do Unsloth
###############################################################################

Configuração realizada:
{'attn_implementation': 'flash_attention_2',
 'device_map': 'auto',
 'dtype': torch.bfloat16,
 'load_in_4bit': True,
 'lora_model': 'lora_model_llama-3-8b-bnb-4bit',
 'max_seq_length': 8192,
 'model': 'unsloth/llama-3-8b-bnb-4bit'}

###############################################################################
# Carregando o modelo e tokenizador para o modelo...
###############################################################################

==((====))==  Unsloth 2025.1.5: Fast Llama patching. Transformers: 4.49.0.
   \\   /|    GPU: NVIDIA GeForce RTX 4060 Laptop GPU. Max memory: 7.996 GB. Platform: Windows.
O^O/ \_/ \    Torch: 2.6.0+cu126. CUDA: 8.9. CUDA Toolkit: 12.6. Triton: 3.2.0
\        /    Bfloat16 = TRUE. FA [Xformers = 0.0.29.post3. FA2 = False]
 "-____-"     Free Apache license: http://github.com/unslothai/unsloth
Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\.venv\Lib\site-packages\unsloth\models\llama.py:1185: UserWarning: expandable_segments not supported on this platform (Triggered internally at C:\actions-runner\_work\pytorch\pytorch\pytorch\c10/cuda/CUDAAllocatorConfig.h:28.)
  self.register_buffer("cos_cached", emb.cos().to(dtype=dtype, device=device, non_blocking=True), persistent=False)

Modelo unsloth/llama-3-8b-bnb-4bit e tokenizador carregados e com sucesso!

###############################################################################
# Configurando o modelo para fine-tuning com LoRA (Low Rank Adaptation)...
###############################################################################

Unsloth 2025.1.5 patched 32 layers with 32 QKV layers, 32 O layers and 32 MLP layers.

Modelo configurado para fine-tuning com LoRA (Low Rank Adaptation)

###############################################################################
# Criando o Conjunto de Dados para Treinamento do Modelo...
###############################################################################

Processando linhas: 100%|███████████████████████████████████████████████| 5002/5002 [00:00<00:00, 277916.39it/s] 

###############################################################################
# Gerando o Arquivo com o Conjunto de Dados para Treinamento do Modelo...
###############################################################################

Salvando registros: 100%|███████████████████████████████████████████████| 5000/5000 [00:00<00:00, 5001554.97it/s] 

Dataset salvo em                             : trn_processed_dataset.json

###############################################################################
# Gerando o Dataset para Treinamento do Modelo...
###############################################################################

Generating train split: 5000 examples [00:00, 59244.76 examples/s]

Dataset geardo com sucesso: Dataset({
    features: ['instruction', 'input', 'output'],
    num_rows: 5000
})

###############################################################################
# Convertendo o Dataset para Treinamento do Modelo em Prompts...
###############################################################################

Formatando prompts: 100%|███████████████████████████████████████████████| 5000/5000 [00:00<00:00, 70249.52 examples/s]

Dataset convertido com sucesso: Dataset({
    features: ['instruction', 'input', 'output', 'text'],
    num_rows: 5000
})

###############################################################################
# Configurando o Treinador SFT (Supervised Fine-Tuning)...
###############################################################################

Map: 100%|████████████████████████████████████████████████████████| 5000/5000 [00:00<00:00, 6432.07 examples/s]
No label_names provided for model class `PeftModelForCausalLM`. Since `PeftModel` hides base models input arguments, if label_names is not given, label_names can't be set automatically within `Trainer`. Note that empty label_names list will be used instead.       

Treinador SFT configurado com sucesso!

###############################################################################
# Treinando o Treinador SFT (Supervised Fine-Tuning)...
###############################################################################

==((====))==  Unsloth - 2x faster free finetuning | Num GPUs = 1
   \\   /|    Num examples = 5,000 | Num Epochs = 1
O^O/ \_/ \    Batch size per device = 2 | Gradient Accumulation steps = 4
\        /    Total batch size = 8 | Total steps = 60
 "-____-"     Number of trainable parameters = 83,886,080
{'loss': 3.2363, 'grad_norm': 1.2131766080856323, 'learning_rate': 4e-05, 'epoch': 0.0}
{'loss': 3.2404, 'grad_norm': 0.872961163520813, 'learning_rate': 8e-05, 'epoch': 0.0}
{'loss': 3.27, 'grad_norm': 1.1601091623306274, 'learning_rate': 0.00012, 'epoch': 0.0}   
{'loss': 3.0758, 'grad_norm': 0.9473162889480591, 'learning_rate': 0.00016, 'epoch': 0.01}
{'loss': 3.1607, 'grad_norm': 0.8515984416007996, 'learning_rate': 0.0002, 'epoch': 0.01}
{'loss': 2.9793, 'grad_norm': 1.187525987625122, 'learning_rate': 0.00019636363636363636, 'epoch': 0.01}
{'loss': 2.7279, 'grad_norm': 0.8072238564491272, 'learning_rate': 0.00019272727272727274, 'epoch': 0.01}
{'loss': 2.8233, 'grad_norm': 0.8448505997657776, 'learning_rate': 0.0001890909090909091, 'epoch': 0.01}
{'loss': 2.4666, 'grad_norm': 0.8008617162704468, 'learning_rate': 0.00018545454545454545, 'epoch': 0.01}
{'loss': 2.4212, 'grad_norm': 1.114966630935669, 'learning_rate': 0.00018181818181818183, 'epoch': 0.02}
{'loss': 1.9802, 'grad_norm': 1.2337411642074585, 'learning_rate': 0.0001781818181818182, 'epoch': 0.02}
{'loss': 2.1742, 'grad_norm': 1.1017382144927979, 'learning_rate': 0.00017454545454545454, 'epoch': 0.02}
{'loss': 2.3788, 'grad_norm': 0.8992886543273926, 'learning_rate': 0.0001709090909090909, 'epoch': 0.02}
{'loss': 2.0038, 'grad_norm': 1.1237659454345703, 'learning_rate': 0.00016727272727272728, 'epoch': 0.02}
{'loss': 2.0972, 'grad_norm': 0.9411469101905823, 'learning_rate': 0.00016363636363636366, 'epoch': 0.02}
{'loss': 2.1032, 'grad_norm': 0.9586315155029297, 'learning_rate': 0.00016, 'epoch': 0.03}
{'loss': 2.1533, 'grad_norm': 0.8134886622428894, 'learning_rate': 0.00015636363636363637, 'epoch': 0.03}
{'loss': 2.2053, 'grad_norm': 0.6734733581542969, 'learning_rate': 0.00015272727272727275, 'epoch': 0.03}
{'loss': 2.1009, 'grad_norm': 1.0051190853118896, 'learning_rate': 0.0001490909090909091, 'epoch': 0.03}
{'loss': 2.2186, 'grad_norm': 0.7856699228286743, 'learning_rate': 0.00014545454545454546, 'epoch': 0.03}
{'loss': 1.8465, 'grad_norm': 1.0131114721298218, 'learning_rate': 0.00014181818181818184, 'epoch': 0.03}
{'loss': 2.3919, 'grad_norm': 0.6858813762664795, 'learning_rate': 0.0001381818181818182, 'epoch': 0.04}
{'loss': 2.0817, 'grad_norm': 1.1349540948867798, 'learning_rate': 0.00013454545454545455, 'epoch': 0.04}
{'loss': 2.3466, 'grad_norm': 0.632728636264801, 'learning_rate': 0.00013090909090909093, 'epoch': 0.04}
{'loss': 2.3803, 'grad_norm': 0.7519182562828064, 'learning_rate': 0.00012727272727272728, 'epoch': 0.04}
{'loss': 2.2041, 'grad_norm': 0.6896740794181824, 'learning_rate': 0.00012363636363636364, 'epoch': 0.04}
{'loss': 2.2582, 'grad_norm': 0.6328169703483582, 'learning_rate': 0.00012, 'epoch': 0.04}
{'loss': 2.1671, 'grad_norm': 0.7278182506561279, 'learning_rate': 0.00011636363636363636, 'epoch': 0.04}
{'loss': 2.0451, 'grad_norm': 0.740135669708252, 'learning_rate': 0.00011272727272727272, 'epoch': 0.05}
{'loss': 2.1491, 'grad_norm': 0.7740330100059509, 'learning_rate': 0.00010909090909090909, 'epoch': 0.05}
{'loss': 2.109, 'grad_norm': 0.8289688229560852, 'learning_rate': 0.00010545454545454545, 'epoch': 0.05}
{'loss': 2.3633, 'grad_norm': 0.6636803150177002, 'learning_rate': 0.00010181818181818181, 'epoch': 0.05}
{'loss': 2.1169, 'grad_norm': 0.8273627758026123, 'learning_rate': 9.818181818181818e-05, 'epoch': 0.05}
{'loss': 2.0114, 'grad_norm': 0.8621428608894348, 'learning_rate': 9.454545454545455e-05, 'epoch': 0.05}
{'loss': 2.0144, 'grad_norm': 0.7383589744567871, 'learning_rate': 9.090909090909092e-05, 'epoch': 0.06}
{'loss': 2.257, 'grad_norm': 0.7085612416267395, 'learning_rate': 8.727272727272727e-05, 'epoch': 0.06}
{'loss': 2.1334, 'grad_norm': 0.7332112193107605, 'learning_rate': 8.363636363636364e-05, 'epoch': 0.06}
{'loss': 1.8868, 'grad_norm': 0.92313152551651, 'learning_rate': 8e-05, 'epoch': 0.06}
{'loss': 2.4323, 'grad_norm': 0.7163751721382141, 'learning_rate': 7.636363636363637e-05, 'epoch': 0.06}
{'loss': 2.1099, 'grad_norm': 0.6877467036247253, 'learning_rate': 7.272727272727273e-05, 'epoch': 0.06}
{'loss': 2.347, 'grad_norm': 0.5720047354698181, 'learning_rate': 6.90909090909091e-05, 'epoch': 0.07}  
{'loss': 2.1136, 'grad_norm': 0.7596690654754639, 'learning_rate': 6.545454545454546e-05, 'epoch': 0.07}
{'loss': 2.0988, 'grad_norm': 0.905095636844635, 'learning_rate': 6.181818181818182e-05, 'epoch': 0.07} 
{'loss': 1.654, 'grad_norm': 0.6866092085838318, 'learning_rate': 5.818181818181818e-05, 'epoch': 0.07} 
{'loss': 2.0823, 'grad_norm': 0.7817774415016174, 'learning_rate': 5.4545454545454546e-05, 'epoch': 0.07}
{'loss': 2.1367, 'grad_norm': 0.7221857905387878, 'learning_rate': 5.090909090909091e-05, 'epoch': 0.07}
{'loss': 1.88, 'grad_norm': 0.8927267789840698, 'learning_rate': 4.7272727272727275e-05, 'epoch': 0.08} 
{'loss': 2.1498, 'grad_norm': 0.7842603921890259, 'learning_rate': 4.3636363636363636e-05, 'epoch': 0.08}
{'loss': 2.314, 'grad_norm': 0.7767072916030884, 'learning_rate': 4e-05, 'epoch': 0.08}                 
{'loss': 2.3262, 'grad_norm': 0.6828826069831848, 'learning_rate': 3.6363636363636364e-05, 'epoch': 0.08}
{'loss': 2.2895, 'grad_norm': 0.6820551156997681, 'learning_rate': 3.272727272727273e-05, 'epoch': 0.08}
{'loss': 1.8453, 'grad_norm': 1.0314183235168457, 'learning_rate': 2.909090909090909e-05, 'epoch': 0.08}
{'loss': 2.155, 'grad_norm': 0.6661691069602966, 'learning_rate': 2.5454545454545454e-05, 'epoch': 0.08}
{'loss': 2.2089, 'grad_norm': 0.7872574925422668, 'learning_rate': 2.1818181818181818e-05, 'epoch': 0.09}
{'loss': 2.0184, 'grad_norm': 0.7385064959526062, 'learning_rate': 1.8181818181818182e-05, 'epoch': 0.09}
{'loss': 2.0609, 'grad_norm': 0.6207361817359924, 'learning_rate': 1.4545454545454545e-05, 'epoch': 0.09}
{'loss': 2.2091, 'grad_norm': 0.6023378372192383, 'learning_rate': 1.0909090909090909e-05, 'epoch': 0.09}
{'loss': 1.7463, 'grad_norm': 0.5827916264533997, 'learning_rate': 7.272727272727272e-06, 'epoch': 0.09}
{'loss': 1.7631, 'grad_norm': 1.0372639894485474, 'learning_rate': 3.636363636363636e-06, 'epoch': 0.09}
{'loss': 1.6957, 'grad_norm': 0.7620051503181458, 'learning_rate': 0.0, 'epoch': 0.1} 
{'train_runtime': 364.4972, 'train_samples_per_second': 1.317, 'train_steps_per_second': 0.165, 'train_loss': 2.253616464138031, 'epoch': 0.1}
100%|███████████████████████████████████████████████████████████████████| 60/60 [06:04<00:00,  6.07s/it] 

Estatísticas do Treinamento
===========================
Tempo total de treinamento       : 364.50 segundos (6.07 min)
Velocidade de processamento      : 1.32 samples/s
Loss final do treinamento        : 2.2536

Estatísticas de Memória GPU
============================
Pico de memória reservada        : 8.074 GB
Pico de memória para treinamento : 0.000 GB
Percentual da memória máxima     : 100.975%
Percentual usado no treinamento  : 0.000%

AVISO: O uso de memória ultrapassou o limite máximo recomendado!

Treinamento concluido com sucesso!

###############################################################################
# Preparando o modelo para fazer inferência (previsões)...
###############################################################################

Modelo preparado para inferência!

###############################################################################
# Preparando 'Mog's Kittens' para ser tokenizado e passar por inferência...
###############################################################################

Tokenização realizada com sucesso!

###############################################################################
# Realizando pergunta para o modelo...
###############################################################################

Resposta obtida com sucesso!

Resposta do modelo: [The New York Times bestselling author of the beloved Mog series returns with a new tale of a cat and her kittens  Mog is a cat who loves to sleep in the sun and eat tuna fish But when she has kittens of her own she must learn to be a good mother and teach her kittens to be good cats too  This is a sweet and funny story about a cat and her kittens that is sure to delight young readers  Ages 3 to 7]

###############################################################################
# Preparando 'Mog's Kittens' para ser tokenizado e passar por inferência...
###############################################################################

Tokenização realizada com sucesso!
 The New York Times bestselling author of the beloved Mog series returns with a new story about the little cat who has charmed millions of readers worldwideMog is a cat who likes to be in charge of things Mog likes to be in charge of the other cats Mog likes to be
 in charge of the dog Mog likes to be in charge of the fish Mog likes to be in charge of the bird Mog likes to be in charge of the mouse Mog likes to be in charge of the baby Mog likes to be in charge of the worldBut when the baby is born Mog finds that being in charge is not as easy as she thought it would beM

Resposta obtida com sucesso!

###############################################################################
# Salvando o Modelo Treinado em lora_model_llama-3-8b-bnb-4bit...
###############################################################################
Unsloth: Merging 4bit and LoRA weights to 16bit...
Unsloth: Will use up to 0.0 out of 31.73 RAM for saving.
Unsloth: Saving model... This might take 5 minutes ...
  0%|                                                    | 0/32 [00:00<?, ?it/s] 
We will save to Disk and not RAM now.
100%|████████████████████████████████████████████████████| 32/32 [01:31<00:00,  2.85s/it]
Unsloth: Saving tokenizer... Done.
Done.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM DO FINE-TUNING <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''

## Testando Modelo Treinado

Nosso código para o treinamento do modelo está disponível no arquivo 
"ft_test_trained_model.py".

O proceso de fine-tuning é feito a partir do arquivo processado 
(trn_processed.json) na fase de preparação dos dados para treinamento.


'''
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge> python .\ft_test_trained_model.py
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
🦥 Unsloth Zoo will now patch everything to make training faster!

###############################################################################
# Criando Configurações do Unsloth
###############################################################################

Configuração realizada:
{'attn_implementation': 'flash_attention_2',
 'device_map': 'auto',
 'dtype': torch.bfloat16,
 'load_in_4bit': True,
 'lora_model': 'lora_model_llama-3-8b-bnb-4bit',
 'max_seq_length': 8192,
 'model': 'unsloth/llama-3-8b-bnb-4bit'}

###############################################################################
# Perguntando ao modelo treinado: ./lora_model_llama-3-8b-bnb-4bit
###############################################################################

The `load_in_4bit` and `load_in_8bit` arguments are deprecated and will be removed in the future versions. Please, pass a `BitsAndBytesConfig` object in `quantization_config` argument instead.
`low_cpu_mem_usage` was None, now default to True since model is quantized.
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\.venv\Lib\site-packages\accelerate\utils\modeling.py:330: UserWarning: expandable_segments not supported on this platform (Triggered internally at C:\actions-runner\_work\pytorch\pytorch\pytorch\c10/cuda/CUDAAllocatorConfig.h:28.)
  new_value = value.to(device)

Query:  Girls Ballet Tutu Neon Blue

Resposta do modelo:
 The perfect gift for the little ballerina in your life this tutu is made of soft nylon tulle and is fully lined with a satin drawstring waistband<|end_of_text|>

Query:  Mog's Kittens

Resposta do modelo:
 Praise for Mog the Forgetful Catx2018Grandparents are likely to get as much fun out of seeing it again as the new generation of fans just learning to readx2019 Choice Magazinex2018A lovely book for all Mogfanciersx2019 The Observerx2018Kerrx2019s watercolours are
 full of humour and expressionx2019 Financial Timesx2018A lovely book for all Mogfanciersx2019 The Observerx2018Kerrx2019s watercolours are full of humour and expressionx2019 Financial Times<|end_of_text|>

Query:  The Prophet

Resposta do modelo:
 The Prophet is a book of 26 prose poetry essays written in English by LebaneseAmerican artist Kahlil Gibran 1883ndash1931 The Prophet has been translated into over 20 languages and has sold more than 100 million copies worldwide<|end_of_text|>

Query:  The Book of Revelation

Resposta do modelo:
 The Book of Revelation is the last book of the New Testament and one of the most enigmatic and controversial works in Western literature It is a book of apocalyptic prophecy that predicts the end of the world and the Last Judgment The book is also known as the Apocalypse of John or simply the Apocalypse<|end_of_text|>
'''

# RAG

O processo de RAG (Retrieval Augmented Generation) do modelo envolve duas 
etapas: na primeira, realizamos a indexação dos dados que iremos trabalhar
com o modelo de IA escolhido ("unsloth/llama-3-8b-bnb-4bit") enquanto na 
segunda, interrogamos o modelo utilizando a base de dados indexada, utilizando  
RAG.
Uma etapa intermediária foi introduzida, apenas para verificar a indexação dos 
dados de trabalho (trn_processed.json). 

## Indexação dos Dados

Nosso código para a indexação dos dados para realização e RAG está disponível no
arquivo "rag_indexing.py".

O início do processo se dá com o consumo do arquivo "trn_processed.json". Ele é 
carregado para que seus dados sejam preparados para a indexação na vector store
(ChromaDB). Para otimizar as busca, os dados são quebrados em pedaçoes menores 
(chunks), antes de serem convertidos em vetores de embeddings. Com os embeddings
gerados, chegou o momento de converter os dados processados em documentos que 
serão armazenados na vector store. Tendo os documentos prontamente convertidos, 
chegou o momento de instanciar a vector store e então armazenar documentos e 
embeddings criados.  

## Exemplo de execução:


## Verificação dos Dados Indexados (Passo Intermediário)
Nosso código para a verificação dos dados que foram indexados anteriormente está
disponível no arquivo "rag_search_vs.py".

## Exemplo de execução:

## Testando o Modelo com RAG
Nosso código para a realização de consultas ao modelo, utilizando RAG está 
disponível no arquivo "rag_model_retriever.py".

## Exemplo de execução:
