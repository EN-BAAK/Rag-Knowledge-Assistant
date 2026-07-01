import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embeddings, documents):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.documents.extend(documents)

    def search(self, query_vector, k=3):
        query = np.array([query_vector]).astype("float32")
        _, indices = self.index.search(query, k)

        results = []
        for idx in indices[0]:
            results.append(self.documents[idx])

        return results