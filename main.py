from src import load_pdf, create_chunks, EmbeddingModel, VectorStore

pdf_path = "./data/pdfs/attention_is_all_you_need.pdf"

documents = load_pdf(pdf_path)

chunks = create_chunks(documents, chunk_size=500, chunk_overlap=50)
texts = [c["text"] for c in chunks]

embedding_model = EmbeddingModel()
vectors = embedding_model.embed_documents(texts)

print("Embedding shape:", vectors.shape)

db = VectorStore(dimension=vectors.shape[1])
db.add(vectors, chunks)

question = "What is attention mechanism?"
query_vector = embedding_model.embed_query(question)
results = db.search(query_vector, k=3)

print("\nTop results:\n")
for r in results:
    print("PAGE:", r["page"])
    print(r["text"][:300])
    print("----------------")