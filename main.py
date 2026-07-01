from src import RAGPipeline

PDF = "./data/pdfs"
VECTOR_DB = "./vector_db"

rag = RAGPipeline(
    pdf__folder=PDF,
    chunk_overlap=50,
    chunk_size=500,
    top_k=3,
    vector_db_path=VECTOR_DB
)

rag.load()

question = input("What is your question? \n")
answer = rag.ask(question)

print("Answer:", answer)