import torch
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
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

# Carrega o modelo base
def get_model(base_model):
    model = AutoPeftModelForCausalLM.from_pretrained(
        base_model, # YOUR MODEL YOU USED FOR TRAINING
        load_in_4bit = load_in_4bit,
    )
    return model

def get_tokenizer(base_model):
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    return tokenizer


def get_inputs(tokenizer, product):
    # Tokeniza e move para GPU
    inputs = tokenizer(
        # Lista com os prompts
        [  
            # Formata o prompt usando template Alpaca
            alpaca_prompt.format(
                "GET THE DESCRIPTION OF THIS PRODUCT", # Instrução
                product,                               # Produto
                "",                                    # Resposta vazia
            ),
        ],
        padding=True,
        truncation=True,
        return_tensors = "pt"  # Retorna tensores PyTorch 
    ).to("cuda")  # Move para GPU
    return inputs             

def get_text_streamer(tokenizer):
    text_streamer = TextStreamer(tokenizer, skip_prompt=True)
    return text_streamer

def get_outputs(model, inputs, text_streamer):
    # Gera resposta
    print("\nResposta do modelo:")
    outputs = model.generate(
        **inputs,
        streamer = text_streamer,
        max_new_tokens = 128,
        temperature = 0.8,
        do_sample = True
    )
    return outputs

    # Decodifica os tokens em texto
def decode_responses(tokenizer, outputs):
    responses = tokenizer.batch_decode(outputs)
    return responses

def ask_the_model(base_model, product):
    model = get_model(base_model)
    tokenizer = get_tokenizer(base_model)
    inputs = get_inputs(tokenizer, product)
    text_streamer = get_text_streamer(tokenizer)
    outputs = get_outputs(model, inputs, text_streamer)
    decode_responses(tokenizer, outputs)

def ask_questions_to_the_model(base_model):
    model = get_model(base_model)
    tokenizer = get_tokenizer(base_model)
    questions = ["Girls Ballet Tutu Neon Blue",
                 "Mog's Kittens",
                 "The Prophet",
                 "The Book of Revelation"]
    for question in questions:
        inputs = get_inputs(tokenizer, question)
        text_streamer = get_text_streamer(tokenizer)
        outputs = get_outputs(model, inputs, text_streamer)
        decode_responses(tokenizer, outputs)

base_model = "./lora_model_llama-3-8b-bnb-4bit"

# ask_the_model(base_model, "Girls Ballet Tutu Neon Blue")
# ask_the_model(base_model, "Mog's Kittens")
# ask_the_model(base_model, "The Prophet")
# ask_the_model(base_model, "The Book of Revelation")

ask_questions_to_the_model(base_model)
