from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = []
    chunk_id = 0

    for doc in documents:
        split_texts = splitter.split_text(doc["text"])

        for text in split_texts:
            chunks.append(
                {
                "chunk_id": chunk_id,
                "source": doc["source"],
                "page": doc["page"],
                "text": text
                }
            )

            chunk_id += 1

    return chunks