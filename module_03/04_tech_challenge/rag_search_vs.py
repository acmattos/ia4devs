from rag_indexing import create_embeddings_model, create_vector_store 

embeddings_model = create_embeddings_model()
vector_store = create_vector_store(embeddings_model)

print("\nRealizando consultas na vector_store")
results = vector_store.similarity_search_by_vector(
    embedding=embeddings_model.embed_query("Girls Ballet Tutu Neon Pink"), k=3
)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")

