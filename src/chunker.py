from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = []

    for doc in documents:
        split_texts = splitter.split_text(doc["text"])

        for text in split_texts:
            chunks.append(
                {
                    "page": doc["page"],
                    "text": text,
                }
            )

    return chunks