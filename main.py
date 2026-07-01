from src import load_pdf, create_chunks, EmbeddingModel, VectorStore, LLM

pdf_path = "./data/pdf_files/attention.pdf"

documents = load_pdf(pdf_path)

chunks = create_chunks(
    documents,
    chunk_size=500,
    chunk_overlap=50
)

texts = [c["text"] for c in chunks]

embedding_model = EmbeddingModel()
vectors = embedding_model.embed_documents(texts)

db = VectorStore(dimension=vectors.shape[1])
db.add(vectors, chunks)

question = "What is attention mechanism?"
query_vector = embedding_model.embed_query(question)

retrieved_chunks = db.search(query_vector, k=4)

context = "\n\n".join(
    [
        f"[PAGE {c['page']}]: {c['text']}"
        for c in retrieved_chunks
    ]
)

prompt = f"""
CONTEXT:
{context}

QUESTION:
{question}

INSTRUCTIONS:
- Answer ONLY using the context above
- If the answer is not in the context, say "I don't know"
- Be precise and technical
"""

llm = LLM()
answer = llm.generate(prompt)

print("\n" + "="*50)
print("QUESTION:")
print(question)

print("\n" + "="*50)
print("ANSWER:")
print(answer)

print("\n" + "="*50)
print("RETRIEVED CHUNKS:")
for c in retrieved_chunks:
    print(f"\nPAGE {c['page']}")
    print(c['text'][:200] + "...")