from src import EmbeddingModel, LLM, load_all_pdfs, create_chunks, VectorStore

class RAGPipeline:
    def __init__(self, pdf__folder, chunk_size=500, chunk_overlap=50, vector_db_path="./vector_db", top_k=4):
        self.pdf_folder = pdf__folder
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.vector_db_path = vector_db_path
        self.top_k = top_k

        self.db = None
        self.embedding_model = EmbeddingModel()
        self.llm = LLM()

    def build(self):
        documents = load_all_pdfs(self.pdf_folder)

        chunks = create_chunks(
            documents,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

        texts = [c["text"] for c in chunks]
        vectors = self.embedding_model.embed_documents(texts)

        db = VectorStore(dimension=vectors.shape[1])
        db.add(vectors, chunks)
        db.save(self.vector_db_path)
        self.db = db

    def ask(self, question):
        query_vector= self.embedding_model.embed_query(question)
        results = self.db.search(query_vector, k=self.top_k)

        context = "\n\n".join([r["text"] for r in results])
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

        print("Context:", context)
        answer = self.llm.generate(prompt)
        return answer