from rag_indexing import create_embeddings_model, create_vector_store
#from fine_tuning import create_alpaca_prompt 
from unsloth import FastLanguageModel
import torch

embeddings_model = create_embeddings_model()
vector_store = create_vector_store(embeddings_model)
retriever = vector_store.as_retriever(search_kwargs={"k":3})

# --- 3. Carregamento do Modelo unsloth ---
max_seq_length = 2048
dtype = torch.bfloat16  
load_in_4bit = True

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/llama-3-8b-bnb-4bit",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
    device_map={"": "cuda:0"}
)
# Adiciona esta linha para preparar o modelo para inferência
model = FastLanguageModel.for_inference(model)
print("Modelo unsloth carregado com sucesso!")

# Template no estilo Alpaca: a resposta está em branco para que o modelo a gere
#alpaca_prompt = create_alpaca_prompt()
alpaca_prompt = """
Below is an instruction that describes a task, paired with an input that 
provides further context. Write a response that appropriately completes 
the request.

### Instruction:
{} {}

### Input:
{}

### Response:
{}
"""
#Função RAG com Prompt Alpaca 
# # def rag_generate(query):
# Recupera documentos relevantes usando o retriever
product = "Girls Ballet Tutu Neon Blue"
retrieved_docs = retriever.get_relevant_documents(product)

# Concatena o conteúdo dos documentos recuperados (ajuste a formatação se necessário)
context = "\n".join([doc.page_content if hasattr(doc, "page_content") else doc for doc in retrieved_docs])

# Usa o template Alpaca para compor o prompt:
#   - Instruction: a query ou uma instrução genérica para o modelo
#   - Input: o contexto recuperado
#   - Response: string vazia, para que o modelo gere a resposta

prompt = alpaca_prompt.format("GET THE DESCRIPTION OF THIS PRODUCT:", product, context, "")

# Tokeniza o prompt com padding e truncation
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=max_seq_length)
inputs = {key: value.to("cuda:0") for key, value in inputs.items()}

## Geração da resposta – ajuste os parâmetros conforme necessário
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length   = 512,
        do_sample    = True,
        temperature  = 0.1,
        top_p        = 0.95,
        pad_token_id = tokenizer.eos_token_id,
    )

answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

#--- 6. Teste da Pipeline RAG com Prompt Alpaca ---
print("\n\nResposta gerada 0.1:")
def extract_response(answer):
    """
    Extrai e retorna o texto após "### Response:" da resposta gerada.
    
    Args:
    - answer (str): A resposta gerada, que contém o texto após "### Response:".
    
    Returns:
    - response_text (str): O texto após "### Response:".
    """
    # Procurando pela linha "### Response:" e extraindo o conteúdo após ela
    response_start = "### Response:"
    if response_start in answer:
        # Encontra o índice onde "### Response:" começa
        start_index = answer.index(response_start) + len(response_start)
        # Extrai o texto após "### Response:"
        response_text = answer[start_index:].strip()
        return response_text
    else:
        return "Nenhuma resposta encontrada."

print(answer)
# Extrair a resposta
response_text = extract_response(answer)
print("\n\nResposta:", response_text)


################################################################################
# Função RAG com Prompt Alpaca
# # def rag_generate(query):
# Recupera documentos relevantes usando o retriever
product = "Mog's Kittens"
retrieved_docs = retriever.get_relevant_documents(product)

# Concatena o conteúdo dos documentos recuperados (ajuste a formatação se necessário)
context = "\n".join(
    [doc.page_content if hasattr(doc, "page_content") else doc for doc in
     retrieved_docs])

# Usa o template Alpaca para compor o prompt:
#   - Instruction: a query ou uma instrução genérica para o modelo
#   - Input: o contexto recuperado
#   - Response: string vazia, para que o modelo gere a resposta

prompt = alpaca_prompt.format("GET THE DESCRIPTION OF THIS PRODUCT:", product,
                              context, "")

# Tokeniza o prompt com padding e truncation
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True,
                   max_length=max_seq_length)
inputs = {key: value.to("cuda:0") for key, value in inputs.items()}

## Geração da resposta – ajuste os parâmetros conforme necessário
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length=512,
        do_sample=True,
        temperature=0.1,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id,
    )

answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

# --- 6. Teste da Pipeline RAG com Prompt Alpaca ---
print("\n\nResposta gerada 0.1:")


def extract_response(answer):
    """
    Extrai e retorna o texto após "### Response:" da resposta gerada.

    Args:
    - answer (str): A resposta gerada, que contém o texto após "### Response:".

    Returns:
    - response_text (str): O texto após "### Response:".
    """
    # Procurando pela linha "### Response:" e extraindo o conteúdo após ela
    response_start = "### Response:"
    if response_start in answer:
        # Encontra o índice onde "### Response:" começa
        start_index = answer.index(response_start) + len(response_start)
        # Extrai o texto após "### Response:"
        response_text = answer[start_index:].strip()
        return response_text
    else:
        return "Nenhuma resposta encontrada."


print(answer)
# Extrair a resposta
response_text = extract_response(answer)
print("\n\nResposta:", response_text)

# if __name__ == "__main__":
#     main()
