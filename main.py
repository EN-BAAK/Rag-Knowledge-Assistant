from src import create_chunks, load_pdf

pdf_path = "./data/pdfs/attention_is_all_you_need.pdf"

documents = load_pdf(pdf_path)
chunks = create_chunks(documents, chunk_size=500, chunk_overlap=50)

print("Pages:", len(documents))
print("Chunks:", len(chunks))
for i, chunk in enumerate(chunks[:5]):
    print(f"Chunk {i + 1}:")
    print(chunk)
    print()