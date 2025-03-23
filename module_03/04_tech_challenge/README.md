# Preparação do Ambiente

Este trabalho foi planejado para rodar no Windows. Pata isto precisamos ter 
atenção na hora de instalar as bibliotecas e dependências para poder rodar os 
arquivos.

Todos os arquivos rodam no Windows 11 com o Python 3.12.6 em uma GPU RTX 4060. 
Também utilizamos o CUDA 12.6 e cuDNN 9.8. Os passos para instalar os arquivos 
necessários para o trabalho serem executados, podem ser visto abaixo (executar 
na ordem):

* [CUDA Toolkit 12.6](https://developer.nvidia.com/cuda-12-6-3-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)
* [cuDNN 9.8.0 Downloads](https://developer.nvidia.com/cudnn-downloads)
* [triton-windows](https://github.com/woct0rdho/triton-windows)
* [PyTorch](https://pytorch.org/get-started/locally/)
* [Unsloth](https://docs.unsloth.ai/get-started/installing-+-updating/windows-installation)

**Observação**: O Unsloth teve um problema em sua versão 2025.2.X. Para poder 
exeecutar o trabalho, a versão 2025.1.5 teve que ser utilizada.     
  
pip install unsloth==2025.1.5  

Possivelmente a verão de março funcione (não testada):  
  
pip install --no-deps "unsloth>=2025.3.8" "unsloth_zoo>=2025.3.7" --upgrade --force-reinstall
  
# Processamento dos Dados

Os dados utilizados para o trabalho foram obtidos do [The AmazonTitles-1.3MM](https://drive.google.com/file/d/12zH4mL2RX8iSvH0VCNnd3QxO4DzuHWnK/view?usp=sharing).

Em particular, trabalhamos com o arquivo trn.json, que contém os nossos dados de
treino. O arquivo tem este formato:

```json 
{"uid": "0001360000", "title": "Mog's Kittens", "content": "Judith Kerr&#8217;s best&#8211;selling adventures of that endearing (and exasperating) cat Mog have entertained children for more than 30 years. Now, even infants and toddlers can enjoy meeting this loveable feline. These sturdy little board books&#8212;with their bright, simple pictures, easy text, and hand&#8211;friendly formats&#8212;are just the thing to delight the very young. Ages 6 months&#8211;2 years.", "target_ind": [146, 147, 148, 149, 495], "target_rel": [1.0, 1.0, 1.0, 1.0, 1.0]}
{"uid": "0000031895", "title": "Girls Ballet Tutu Neon Blue", "content": "Dance tutu for girls ages 2-8 years. Perfect for dance practice, recitals and performances, costumes or just for fun!", "target_ind": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 31, 33, 42, 46, 54, 58, 111, 113, 125, 126, 159, 163, 202, 203, 204, 205, 206, 207], "target_rel": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}
```
O arquivo trn.json contém 2.248.619 registros. Em particular, vamos trabalhar 
com os campos `title` e `content`. Os demais campos serão descartados.

O arquivos `process_data.py` realiza o processamento dos dados. Vamos descartar 
os registros com `content` vazio ou com o conteúdo menor do que 100 caracteres.
Com isto, geramos o arquivo `trn_processed.json`, com 1.216.560 registros aptos 
a serem usados no treinamento do modelo.

O arquivo tem este formato:

```json 
[
 {"product": "Mogs Kittens", "description": "Judith Kerr8217s best8211selling adventures of that endearing and exasperating cat Mog have entertained children for more than 30 years Now even infants and toddlers can enjoy meeting this loveable feline These sturdy little board books8212with their bright simple pictures easy text and hand8211friendly formats8212are just the thing to delight the very young Ages 6 months82112 years"},
 {"product": "Girls Ballet Tutu Neon Blue", "description": "Dance tutu for girls ages 28 years Perfect for dance practice recitals and performances costumes or just for fun"},
]
```

## Exemplo de execução:
``` 
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge> python .\process_data.py  
  
Lendo os registros do arquivo              : 100%|███████████████| 2248619/2248619 [00:35<00:00, 62903.00it/s]  
Processando registros lidos                : 100%|███████████████| 2248619/2248619 [00:14<00:00, 155615.25it/s]  
Salvando registros processado em arquivo   : 100%|███████████████| 1216560/1216560 [00:10<00:00, 117362.03it/s]  
Total de registros no arquivo original     : 2,248,619  
Total de registros processados (não vazios): 1,216,560  
Arquivo processado salvo em                : trn_processed.json  
```

# Foundation Model
O modelo escolhido para realizar o fine tunning neste trabalho é o 
`unsloth/llama-3-8b-bnb-4bit`. Trata-se de uma implementação otimizada do modelo 
LLaMA (Large Language Model Meta AI), ajustada para ser eficiente em termos de 
memória e desempenho. Ele utiliza quantização em 4 bits, o que reduz 
significativamente o consumo de memória sem comprometer a precisão do modelo. 
Além disso, o modelo é compatível com a biblioteca Hugging Face Transformers e 
foi projetado para ser executado em GPUs com suporte a CUDA, como a NVIDIA 
RTX 4060, aproveitando tecnologias como Flash Attention e LoRA (Low-Rank 
Adaptation) para acelerar o treinamento e a inferência. Com um tamanho de 8 
bilhões de parâmetros, ele é capaz de lidar com tarefas complexas de 
processamento de linguagem natural, como geração de texto, resumo, tradução e 
respostas a perguntas. (Fonte: https://huggingface.co/unsloth/llama-3-8b-bnb-4bit)

O objetivo principal do modelo é permitir o fine-tuning eficiente em cenários 
com recursos computacionais limitados, como laptops ou estações de trabalho com 
GPUs de médio porte. Ele foi otimizado para tarefas que exigem personalização, 
como a adaptação a domínios específicos ou a criação de sistemas de recuperação 
de informações baseados em RAG (Retrieval Augmented Generation). A combinação de 
quantização em 4 bits e adaptadores LoRA permite que o modelo seja ajustado 
rapidamente com conjuntos de dados menores, mantendo alta qualidade nas respostas 
geradas e reduzindo o tempo e os custos associados ao treinamento de modelos grandes.

# Exemplo de execução:

```
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge> python .\foundation_model.py
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
==((====))==  Unsloth 2025.1.5: Fast Llama patching. Transformers: 4.49.0.
   \\   /|    GPU: NVIDIA GeForce RTX 4060 Laptop GPU. Max memory: 7.996 GB. Platform: Windows.
O^O/ \_/ \    Torch: 2.6.0+cu126. CUDA: 8.9. CUDA Toolkit: 12.6. Triton: 3.2.0
\        /    Bfloat16 = TRUE. FA [Xformers = 0.0.29.post3. FA2 = False]
 "-____-"     Free Apache license: http://github.com/unslothai/unsloth
Unsloth: Fast downloading is enabled - ignore downloading bars which are red colored!
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\.venv\Lib\site-packages\unsloth\models\llama.py:1185: 
UserWarning: expandable_segments not supported on this platform (Triggered internally at 
C:\actions-runner\_work\pytorch\pytorch\pytorch\c10/cuda/CUDAAllocatorConfig.h:28.)
  self.register_buffer("cos_cached", emb.cos().to(dtype=dtype, device=device, non_blocking=True), persistent=False)

Produto: Girls Ballet Tutu Neon Blue
Descrição: This is a beautiful tutu. It is made of high quality material and it 
is very comfortable. It is perfect for any occasion and it is very affordable. 
It is also very durable and it will last for a long time. It is also very easy 
to maintain and it is very easy to clean. It is also very easy to wear and it 
is very easy to take off. It is also very easy to put on and it is very easy to 
take off. It is also very easy to put on and it is very easy to take off. It is 
also very easy to put on and it is very easy to take off. It is also very easy 
to put on and it is very easy to take off. It is also very easy to put on and it 
is very easy to take off. It is also very easy to put on and it is very easy to 
take off. It is also very easy to put on and it is very easy to take off. It is 
also very easy to put on and it is very easy to take off. It is also very easy 
to put on and it is very easy to take off. It is also very easy to put on and it 
is very easy to take off. It is also very easy to put on and it is very easy to 
take off. It is also very easy to put on and it is very easy to take off. It is 
also very easy to put on and it is very easy to take off. 

Produto: Mog's Kittens
Descrição: The product is a pair of socks.

Produto: The Prophet
Descrição: The Prophet is a product that helps you to find the best way to spend 
your money. It is a product that helps you to find the best way to spend your 
money. It is a product that helps you to find the best way to spend your money. 
It is a product that helps you to find the best way to spend your money. It is a 
product that helps you to find the best way to spend your money. It is a product 
that helps you to find the best way to spend your money. It is a product that 
helps you to find the best way to spend your money. It is a product that helps 
you to find the best way to spend your money. It is a product that helps you to 
find the best way to spend your money. It is a product that helps you to find 
the best way to spend your money. It is a product that helps you to find the 
best way to spend your money. 

Produto: The Book of Revelation
Descrição: The Book of Revelation is a book of the New Testament of the Bible, 
and its title originated from the first word of the text in the Koine Greek: 
apokalypsis, meaning "unveiling" or "revelation". The author describes himself 
as "John" and does not identify himself as the son of Zebedee, the apostle John. 
The text is a letter to seven churches in the Roman province of Asia, and is a 
call to the churches to remain faithful to Jesus Christ, and individual letters 
to each church, with a promise of a swift punishment for Christian communities 
that are in a state of apostasy. The Book of Revelation is the final book of the 
New Testament and occupies a central place in Christian eschatology. By tradition, 
this prophecy was revealed by its author to the apostle John on the island of 
Patmos, and from its first readers, this prophecy has been accepted as of divine 
inspiration. The author of Revelation does not identify himself, but introduces 
his work as "the revelation of Jesus Christ", which he received "by an angel" from God. 

Process finished with exit code 0
```

# Fine-Tuning

O processo de fine-tuning do modelo envolve duas etapas: na primeira, 
realizamos o fine-tuning do modelo escolhido ("unsloth/llama-3-8b-bnb-4bit") 
enquanto na segunda, interrogamos o modelo treinado 
(./lora_model_llama-3-8b-bnb-4bit).

## Treinamento do Modelo

Nosso código para o treinamento do modelo está disponível no arquivo 
`fine_tuning.py`.

O proceso de fine-tuning é feito a partir do arquivo processado 
`trn_processed.json` na fase de preparação dos dados para treinamento.

O uso do Unsloth e do LoRA foi motivado pela necessidade 
de realizar o fine-tuning de modelos grandes de forma eficiente e com menor 
consumo de recursos computacionais. O Unsloth oferece otimizações específicas 
para acelerar o treinamento, enquanto o LoRA permite ajustar apenas um pequeno 
número de parâmetros, reduzindo significativamente os requisitos de memória e 
tempo de execução, sem comprometer a qualidade do modelo treinado.

Inicialmente, a configuração do Unsloth é feita, de forma a preparar o modelo 
para fine-tuning. Com a configuração pronta, modelo e tokenizador são carregados
e retornado. Depois, aplicamos os adaptadores LoRA ao mesmo modelo, Deixando-o 
pronto para o treinamento.

Neste momento, iniciamos a preparação dos dados que serão utilizados para o 
fine-tuning do modelo. Ele é preparado de forma a agrupar os produtos como 
grupo de entrada (`input`) e as descrições como grupo de saída (`output`). As 
instruções (perguntas que serão feitas ao modelo) ficam no grupo de 
instruções (`instructions`). Esta preparação é salva em arquivo 
(`trn_processed_dataset.json`) para ser utilizada mais adiante.

Além disso, o modelo foi ajustado utilizando o Alpaca, que aprimora a capacidade 
do modelo em lidar com consultas complexas, garantindo respostas mais precisas e 
relevantes, aumentando a eficiência em recuperação de informações e geração de 
textos.

Após ser carregado como um dataset, é transformado em um "prompt dataset"
para ser passado para o treinador do modelo. Então, o treinamento é realizado.
Neste momento, uma mudança de foco precisou ser feita: a quantidade de itens 
a serem treinadas (1.216.560) implicava em um tempo de treinamento que excediam 
7 dias. Com isto, o "prompt dataset" foi reduzido para 5000 item, o que permitiu
a aplicação de duas épocas de treinamento (algo em torno de 1250 iterações) 
tomando um total 2:30 para que a tarefa fosse realizada. É importante ressaltar 
que a configuração presente no código, a GPU utilizada e o conjunto de dados de 
treino influenciam diretamente no tempo de execução do treinamento. Algumas 
estatísticas são mostradas após o treino (tempo gasto, consumo de memória).

Ao finalizarmos esta etapa, preparamos o modelo treinado para a realização de 
inferências. Duas consultas são realizadas, apenas para mostrar as capacidades 
de exibição das respostas às consultas: a exibição completa, após o resultado 
retornado ou sua apresentação conforme o modelo vai gerando a resposta.

Concluído este pequeno teste, salvamos o modelo e seus adaptadores LoRA 
localmente.

O dataset foi carregado e processado de forma a ser compatível com o formato 
esperado pela biblioteca Hugging Face. Isso permite que ele seja utilizado 
diretamente em pipelines de treinamento e inferência, facilitando a integração 
com modelos de aprendizado de máquina e otimizando o fluxo de trabalho.

O modelo treinado fica disponível no seguinte link: 
(ACMattosHE/lora_model_llama-3-8b-bnb-4bit)[https://huggingface.co/ACMattosHE/lora_model_llama-3-8b-bnb-4bit/tree/main]

## Exemplo de execução:
A seguir, o log de execução deste código:

``` 
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
  
Processando linhas: 100%|██████████████| 5002/5002 [00:00<00:00, 277916.39it/s]   
  
###############################################################################  
# Gerando o Arquivo com o Conjunto de Dados para Treinamento do Modelo...  
###############################################################################  
  
Salvando registros: 100%|██████████████| 5000/5000 [00:00<00:00, 5001554.97it/s]  
  
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
  
Formatando prompts: 100%|████████████████| 5000/5000 [00:00<00:00, 70249.52 examples/s]  
  
Dataset convertido com sucesso: Dataset({  
    features: ['instruction', 'input', 'output', 'text'],  
    num_rows: 5000  
})  
  
###############################################################################  
# Configurando o Treinador SFT (Supervised Fine-Tuning)...  
###############################################################################  
  
Map: 100%|██████████████████████████| 5000/5000 [00:00<00:00, 6432.07 examples/s]  
No label_names provided for model class `PeftModelForCausalLM`. Since `PeftModel` 
hides base models input arguments, if label_names is not given, label_names can't 
be set automatically within `Trainer`. Note that empty label_names list will be 
used instead.       
  
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
100%|████████████████████████████████████████████████████████████| 60/60 [06:04<00:00,  6.07s/it]   
   
Estatísticas do Treinamento  
===========================  
Tempo total de treinamento       : 364.50 segundos (6.07 min)  
Velocidade de processamento      : 1.32 samples/s  
Loss final do treinamento        : 2.2536  
  
Estatísticas de Memória GPU  
===========================  
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
  
Resposta do modelo: [The New York Times bestselling author of the beloved Mog 
series returns with a new tale of a cat and her kittens  Mog is a cat who loves 
to sleep in the sun and eat tuna fish But when she has kittens of her own she must 
learn to be a good mother and teach her kittens to be good cats too  This is a 
sweet and funny story about a cat and her kittens that is sure to delight young 
readers  Ages 3 to 7]  
  
###############################################################################  
# Preparando 'Mog's Kittens' para ser tokenizado e passar por inferência...  
###############################################################################  
  
Tokenização realizada com sucesso!  

 The New York Times bestselling author of the beloved Mog series returns with a 
 new story about the little cat who has charmed millions of readers worldwideMog 
 is a cat who likes to be in charge of things Mog likes to be in charge of the 
 other cats Mog likes to be
 in charge of the dog Mog likes to be in charge of the fish Mog likes to be in
  charge of the bird Mog likes to be in charge of the mouse Mog likes to be in 
  charge of the baby Mog likes to be in charge of the worldBut when the baby is
   born Mog finds that being in charge is not as easy as she thought it would beM  
  
Resposta obtida com sucesso!  
  
###############################################################################  
# Salvando o Modelo Treinado em lora_model_llama-3-8b-bnb-4bit...  
###############################################################################  
Unsloth: Merging 4bit and LoRA weights to 16bit...  
Unsloth: Will use up to 0.0 out of 31.73 RAM for saving.  
Unsloth: Saving model... This might take 5 minutes ...  
  0%|                                                    | 0/32 [00:00<?, ?it/s]   
We will save to Disk and not RAM now.  
100%|███████████████████████████████████████████| 32/32 [01:31<00:00,  2.85s/it]  
Unsloth: Saving tokenizer... Done.  
Done.  
  
>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM DO FINE-TUNING <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
```

## Testando Modelo Treinado

Nosso código para o treinamento do modelo está disponível no arquivo 
"ft_test_trained_model.py".

O proceso de fine-tuning é feito a partir do arquivo processado 
(trn_processed.json) na fase de preparação dos dados para treinamento.

## Exemplo de execução:

```
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
  
The `load_in_4bit` and `load_in_8bit` arguments are deprecated and will be 
removed in the future versions. Please, pass a `BitsAndBytesConfig` object in 
`quantization_config` argument instead.  
`low_cpu_mem_usage` was None, now default to True since model is quantized.  
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\.venv\Lib\site-packages\accelerate\utils\modeling.py:330: 
UserWarning: expandable_segments not supported on this platform (Triggered internally at 
C:\actions-runner\_work\pytorch\pytorch\pytorch\c10/cuda/CUDAAllocatorConfig.h:28.)
  new_value = value.to(device)  
  
Query:  Girls Ballet Tutu Neon Blue  
  
Resposta do modelo:  
 The perfect gift for the little ballerina in your life this tutu is made of soft 
 nylon tulle and is fully lined with a satin drawstring waistband<|end_of_text|>  
  
Query:  Mog's Kittens  
  
Resposta do modelo:  
 Praise for Mog the Forgetful Catx2018Grandparents are likely to get as much fun 
 out of seeing it again as the new generation of fans just learning to readx2019 
 Choice Magazinex2018A lovely book for all Mogfanciersx2019 The 
 Observerx2018Kerrx2019s watercolours are
 full of humour and expressionx2019 Financial Timesx2018A lovely book for all 
 Mogfanciersx2019 The Observerx2018Kerrx2019s watercolours are full of humour and 
 expressionx2019 Financial Times<|end_of_text|>  
  
Query:  The Prophet  
  
Resposta do modelo:  
 The Prophet is a book of 26 prose poetry essays written in English by 
 LebaneseAmerican artist Kahlil Gibran 1883ndash1931 The Prophet has been 
 translated into over 20 languages and has sold more than 100 million copies 
 worldwide<|end_of_text|>  
  
Query:  The Book of Revelation  
  
Resposta do modelo:  
 The Book of Revelation is the last book of the New Testament and one of the 
 most enigmatic and controversial works in Western literature It is a book of 
 apocalyptic prophecy that predicts the end of the world and the Last Judgment 
 The book is also known as the Apocalypse of John or simply the Apocalypse<|end_of_text|>  
``` 

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
arquivo `rag_indexing.py`.

O início do processo se dá com o consumo do arquivo `trn_processed.json`. Ele é 
carregado para que seus dados sejam preparados para a indexação na vector store
(ChromaDB). Para otimizar as busca, os dados são quebrados em pedaços menores 
(chunks), antes de serem convertidos em vetores de embeddings. Com os embeddings
gerados, chegou o momento de converter os dados processados em documentos que 
serão armazenados na vector store. Tendo os documentos prontamente convertidos, 
chegou o momento de instanciar a vector store e então armazenar documentos e 
embeddings criados.  

## Exemplo de execução:

```
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge> python .\rag_indexing.py 

Carregando dados do arquivo processado...
Total de registros gerados:5000
Exemplo de registro: 
{'description': 'High quality 3 layer ballet tutu 12 inches in length',
 'product': 'Girls Ballet Tutu Neon Pink'}

Quebrando documentos JSON em chunks...

Total de chunks gerados: 5000

Exemplo de chunk:
Product: Girls Ballet Tutu Neon Pink - Description: High quality 3 layer ballet tutu 12 inches in length

Criando modelo de embeddings...
Dividindo documentos JSON: 100%|██████████| 5000/5000 [00:00<00:00, 555316.30it/s]
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\rag_indexing.py:68: 
LangChainDeprecationWarning: The class `HuggingFaceEmbeddings` was deprecated in 
LangChain 0.2.2 and will be removed in 1.0. An updated version of the class exists 
in the :class:`~langchain-huggingface package and should be used instead. To use 
it run `pip install -U :class:`~langchain-huggingface` and import as `from :class:
`~langchain_huggingface import HuggingFaceEmbeddings``.
  embeddings_model = HuggingFaceEmbeddings(

Criando modelo de embeddings...

Gerando embeddings para os chunks...

Gerando embeddings...

Total de embeddings gerados: 5000

Exemplo de embedding:
[0.03302772715687752,
 -0.021298706531524658,
 -0.021273870021104813,
 0.052845340222120285,
 -0.019837183877825737,
 -0.03264341503381729,
 0.010283859446644783,
 0.014730839990079403,
 -0.017746785655617714,
 0.003939006011933088,
  6.719978057498912e-35,
 0.037213534116744995,
 -0.10796977579593658,
 0.04069541022181511,
 -0.002336055040359497,
 0.006895443890243769,
 -0.05344033241271973,
 0.08863085508346558,
 -0.03707418590784073,
 0.05612768977880478,
 0.00930757075548172,
 -0.023683171719312668]

Convertendo json_data em lc_documents...

C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\rag_indexing.py:122: 
LangChainDeprecationWarning: The class `Chroma` was deprecated in LangChain 0.2.9 
and will be removed in 1.0. An updated version of the class exists in the :class:
`~langchain-chroma package and should be used instead. To use it run `pip install -U :class:
`~langchain-chroma` and import as `from :class:`~langchain_chroma import Chroma``.
  vector_store = Chroma(

Total de lc_documents  gerados: 5000

Exemplo de lc_document:
Document(metadata={'product': 'Girls Ballet Tutu Neon Pink'}, 
page_content='Product: Girls Ballet Tutu Neon Pink - Description: High quality 
3 layer ballet tutu 12 inches in length')

Criando vector_store para o embeddings_model...

vector_store criada!

Populando vector_store...

Gerando UUIDs para cada documento...

Adicionando os documentos no vector_store...

Documentos carregados!
```

## Verificação dos Dados Indexados (Passo Intermediário)
Nosso código para a verificação dos dados que foram indexados anteriormente está
disponível no arquivo `rag_search_vs.py`.

Para realizar a verificação dos dados indexados, utilizamos o modelo de embeddings
criado na indexação dos dados. Em seguida, utilizamos a vector store para realizar
buscas e exibir os resultados.

Os resultados retornados são o 3 mais relevantes ao produto pesquisado. O 
exemplo de execução abaixo mostra os resultados obtidos para o produto
"Girls Ballet Tutu Neon Pink".  

## Exemplo de execução:

```
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge> python .\rag_search_vs.py  
  
Criando modelo de embeddings...  
  
Criando modelo de embeddings...  
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\rag_indexing.py:68:   
LangChainDeprecationWarning: The class `HuggingFaceEmbeddings` was deprecated in   
LangChain 0.2.2 and will be removed in 1.0. An updated version of the class exists   
in the :class:`~langchain-huggingface package and should be used instead. To use it run `  
pip install -U :class:`~langchain-huggingface` and import as   
`from :class:`~langchain_huggingface import HuggingFaceEmbeddings``.  
  embeddings_model = HuggingFaceEmbeddings(  
  
Criando vector_store para o embeddings_model...  
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\rag_indexing.py:122:   
LangChainDeprecationWarning: The class `Chroma` was deprecated in LangChain 0.2.9   
and will be removed in 1.0. An updated version of the class exists in the :class:  
`~langchain-chroma package and should be used instead. To use it run `  
pip install -U :class:`~langchain-chroma` and import as   
`from :class:`~langchain_chroma import Chroma``.  
  vector_store = Chroma(  
  
vector_store criada!  
  
Realizando consultas na vector_store  
  
* Product: Girls Ballet Tutu Neon Blue - Description: Dance tutu for girls ages 
  28 years Perfect for dance practice recitals and performances costumes or just 
  for fun [{'product': 'Girls Ballet Tutu Neon Blue'}]  

* Product: Girls Ballet Tutu Neon Pink - Description: High quality 3 layer ballet 
  tutu 12 inches in length [{'product': 'Girls Ballet Tutu Neon Pink'}]  

* Product: Delphie and the Birthday Show Magic Ballerina Book 6 - Description: 
  x201CDonx2019t be surprised if your child asks for a magical pair of red ballet 
  shoesx201D Telegraph Magazinex201CDelightfulx201D You Magazine Mail on 
  Sundayx201CA delight for any young reader who sees herself as a budding 
  ballerinax201D MumKnowsBestcouk [{'product': 'Delphie and the Birthday Show 
  Magic Ballerina Book 6'}]  
```

## Testando o Modelo com RAG

Nosso código para a realização de consultas ao modelo, utilizando RAG está 
disponível no arquivo "rag_model_retriever.py".

## Exemplo de execução:

```
(.venv) PS C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge> python .\rag_model_retriever.py  
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.  
🦥 Unsloth Zoo will now patch everything to make training faster!  
  
Criando modelo de embeddings...  
  
Criando modelo de embeddings...  
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\rag_indexing.py:68: 
LangChainDeprecationWarning: The class `HuggingFaceEmbeddings` was deprecated in 
LangChain 0.2.2 and will be removed in 1.0. An updated version of the class exists 
in the :class:`~langchain-huggingface package and should be used instead. To use 
it run `pip install -U :class:`~langchain-huggingface` and import as `from :class:
`~langchain_huggingface import HuggingFaceEmbeddings``.  
  embeddings_model = HuggingFaceEmbeddings(  
  
Criando vector_store para o embeddings_model...  
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\rag_indexing.py:122: 
LangChainDeprecationWarning: The class `Chroma` was deprecated in LangChain 0.2.9 
and will be removed in 1.0. An updated version of the class exists in the :class:
`~langchain-chroma package and should be used instead. To use it run `pip install 
-U :class:`~langchain-chroma` and import as `from :class:`~langchain_chroma import Chroma``.  
  vector_store = Chroma(  
  
vector_store criada!  
  
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
  
Modelo unsloth/llama-3-8b-bnb-4bit e tokenizador carregados e com sucesso!  
  
###############################################################################  
# Preparando o modelo para fazer inferência (previsões)...  
###############################################################################  
  
Modelo preparado para inferência!  
C:\acmattos\dev\tools\Python\ia4devs\module_03\04_tech_challenge\rag_model_retriever.py:35: 
LangChainDeprecationWarning: The method `BaseRetriever.get_relevant_documents` 
was deprecated in langchain-core 0.1.46 and will be removed in 1.0. Use :meth:
`~invoke` instead.  
  retrieved_docs = retriever.get_relevant_documents(product)  
  
Resposta gerada:  
  
Below is an instruction that describes a task, paired with an input that   
provides further context. Write a response that appropriately completes   
the request.  
  
### Instruction:  
GET THE DESCRIPTION OF THIS PRODUCT: Girls Ballet Tutu Neon Blue  
  
### Input:  
Product: Girls Ballet Tutu Neon Blue - Description: Dance tutu for girls ages 28 
years Perfect for dance practice recitals and performances costumes or just for fun  
Product: Girls Ballet Tutu Neon Pink - Description: High quality 3 layer ballet 
tutu 12 inches in length  
Product: Delphie and the Birthday Show Magic Ballerina Book 6 - Description: 
x201CDonx2019t be surprised if your child asks for a magical pair of red ballet 
shoesx201D Telegraph Magazinex201CDelightfulx201D You Magazine Mail on Sundayx201CA 
delight for any young reader who sees herself as a budding ballerinax201D MumKnowsBestcouk  

### Response:  

The description of this product is: Girls Ballet Tutu Neon Blue - Description: 
Dance tutu for girls ages 28 years Perfect for dance practice recitals and 
performances costumes or just for fun  

Resposta gerada:  
  
Below is an instruction that describes a task, paired with an input that   
provides further context. Write a response that appropriately completes   
the request.  

### Instruction:  
GET THE DESCRIPTION OF THIS PRODUCT: Mog's Kittens  
  
### Input:  
Product: Mogs Kittens - Description: Judith Kerr8217s best8211selling adventures 
of that endearing and exasperating cat Mog have entertained children for more 
than 30 years Now even infants and toddlers can enjoy meeting this loveable 
feline These sturdy little board books8212with their bright simple pictures easy 
text and hand8211friendly formats8212are just the thing to delight the very young 
Ages 6 months82112 years  
Product: Mog and the VET Mog the Cat Books - Description: Praise for Mog the 
Forgetful Catx2018Grandparents are likely to get as much fun out of seeing it 
again as the new generation of fans just learning to readx2019 Choice Magazinex2018A 
lovely book for all Mogfanciersx2019 The ObserverPraise for Goodbye Mogx2018Kerrx2019s 
warmth humour and honesty make this an engaging introduction to a difficult topicx2019 
Financial Timesx2018Believable amusing and movingx2019 Nursery Worldx2018A supremely 
sensitive storyx2019 The Timesx2018The best most consoling book for children on the 
subject or bereavementx2026a joy to readx2019 The Independent on Sunday   
Product: Mog on Fox Night - Description: Praise for Mog the Forgetful 
Catx2018Grandparents are likely to get as much fun out of seeing it again as the 
new generation of fans just learning to readx2019 Choice Magazinex2018A lovely 
book for all Mogfanciersx2019 The ObserverPraise for Goodbye Mogx2018Kerrx2019s 
warmth humour and honesty make this an engaging introduction to a difficult 
topicx2019 Financial Timesx2018Believable amusing and movingx2019 Nursery 
Worldx2018A supremely sensitive storyx2019 The Timesx2018The best most consoling 
book for children on the subject of bereavementx2026a joy to readx2019 The 
Independent on Sunday  
  
### Response:  
  
Mog's Kittens - Description: Judith Kerr8217s best8211selling adventures of that 
endearing and exasperating cat Mog have entertained children for more than 30 
years Now even infants and toddlers  
```

## Comparação das Respostas dos Modelos

| Produto                     | Modelo Original (Foundation Model)                                                                                       | Modelo com Fine-Tuning                                                                                           | Modelo com RAG                                                                                                   |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Girls Ballet Tutu Neon Blue | This is a beautiful tutu. It is made of high quality material and it is very comfortable. It is perfect for any occasion and it is very affordable. It is also very durable and it will last for a long time. It is also very easy to maintain and it is very easy to clean. It is also very easy to wear and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off. It is also very easy to put on and it is very easy to take off.                              | The perfect gift for the little ballerina in your life this tutu is made of soft  nylon tulle and is fully lined with a satin drawstring waistband                  | Dance tutu for girls ages 28 years. Perfect for dance practice, recitals and performances, costumes or just for fun. |
| Mog's Kittens               | The product is a pair of socks.                                                                                          | Praise for Mog the Forgetful Catx2018Grandparents are likely to get as much fun out of seeing it again as the new generation of fans just learning to readx2019  Choice Magazinex2018A lovely book for all Mogfanciersx2019 The  Observerx2018Kerrx2019s watercolours are full of humour and expressionx2019 Financial Timesx2018A lovely book for all  Mogfanciersx2019 The Observerx2018Kerrx2019s watercolours are full of humour and  expressionx2019 Financial Times                     | Judith Kerr8217s best8211selling adventures of that endearing and exasperating cat Mog have entertained children for more than 30 years Now even infants and toddlers    |
| The Prophet                 | The Prophet is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money. It is a product that helps you to find the best way to spend your money.                                      | The Prophet is a book of 26 prose poetry essays written in English by  LebaneseAmerican artist Kahlil Gibran 1883ndash1931 The Prophet has been  translated into over 20 languages and has sold more than 100 million copies  worldwide  | In a distant timeless place a mysterious prophet walks the sands At the moment of his departure he wishes to offer the people gifts but possesses nothing The people gather round each asks a question of the heart and the mans wisdom is his gift It is Gibrans gift to us as well for Gibrans prophet is rivaled in his wisdom only by the founders of the worlds great religions On the most basic topicsmarriage children friendship work pleasurehis words have a power and lucidity that in another era would surely have provoked the description divinely inspired Free of dogma free of power structures and metaphysics consider these poetic moving aphorisms a 20thcentury supplement to all sacred traditionsas millions of other readers already haveBrian BruyaThis text refers to theHardcoveredition|
| The Book of Revelation      | The Book of Revelation is a book of the New Testament of the Bible, and its title originated from the first word of the text in the Koine Greek: apokalypsis, meaning "unveiling" or "revelation". The author describes himself as "John" and does not identify himself as the son of Zebedee, the apostle John. The text is a letter to seven churches in the Roman province of Asia, and is a call to the churches to remain faithful to Jesus Christ, and individual letters to each church, with a promise of a swift punishment for Christian communities that are in a state of apostasy. The Book of Revelation is the final book of the New Testament and occupies a central place in Christian eschatology. By tradition, this prophecy was revealed by its author to the apostle John on the island of Patmos, and from its first readers, this prophecy has been accepted as of divine inspiration. The author of Revelation does not identify himself, but introduces his work as "the revelation of Jesus Christ", which he received "by an angel" from God.                                                     | The Book of Revelation is the last book of the New Testament and one of the most enigmatic and controversial works in Western literature It is a book of  apocalyptic prophecy that predicts the end of the world and the Last Judgment  The book is also known as the Apocalypse of John or simply the Apocalypse  | American Baptist pastor Bible teacher and writer Clarence Larkin was born October 28 1850 in Chester Delaware County Pennsylvania He was converted to Christ at the age of 19 and then felt called to the Gospel ministry but the doors of opportunity for study and ministry did not open immediately He then got a job in a bank When he was 21 years old he left the bank and went to college graduating as a mechanical engineer He continued as a professional draftsman for a while then he became a teacher of the blind Later failing health compelled him to give up his teaching career After a prolonged rest he became a manufacturer When he was converted he had become a member of the Episcopal Church but in 1882he became a Baptist and was ordained as a Baptist minister two years later He went directly from business into the ministry His first charge was at Kennett Square Pennsylvania his second pastorate was at Fox Chase Pennsylvania where he remained for 20 years He was not a premillennialist at the time of his ordination but his study of the Scriptures with the help of some books that fell into his hands led him to adopt the premillennialist position He began to make large wall charts which he titled Prophetic Truth for use in the pulpit These led to his being invited to teach in connection with his pastoral work in two Bible institutes During this time he published a number of prophetical charts which were widely circulated When World War I broke out in 1914 he was called on for addresses on The War and Prophecy Then God laid it on his heart to prepare a work on Dispensational Truth or Gods Plan and Purpose in the Ages containing a number of charts with descriptive matter He spent three years of his life designing and drawing the charts and preparing the text The favorable reception it has had since it was first published in 1918 seems to indicate that the world was waiting for such a book Because it had a large and wide circulation in this and other lands the first edition was soon exhausted It was followed by a second edition and then realizing that the book was of permanent value Larkin revised it and expanded it printing it in its present form He went to be with the Lord on January 24 1924This text refers to thePaperbackedition|

**Observações:**
- O modelo com fine-tuning apresenta respostas mais detalhadas e relevantes em 
  comparação ao modelo original.
- O modelo com RAG utiliza a base de dados indexada para fornecer respostas mais 
  precisas e contextualizadas, mas está limitado aos dados previamente indexados.
- O modelo original (Foundation Model) apresenta respostas genéricas e, em alguns 
  casos, completamente irrelevantes, como no exemplo de "Mog's Kittens", onde a 
- resposta foi "The product is a pair of socks".
- O modelo com fine-tuning demonstra uma melhoria significativa na qualidade das 
  respostas, mas ainda apresenta redundâncias ou informações desnecessárias em 
  alguns casos.
- O modelo com RAG é altamente dependente da qualidade e abrangência dos dados 
  indexados. Ele é ideal para cenários onde as informações relevantes estão 
  contidas em uma base de dados específica.