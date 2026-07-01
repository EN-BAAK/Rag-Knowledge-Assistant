import json

from src import RAGPipeline

PDF = "./data/pdfs"
EXP = "./experiments/test_quesitons.json"

configs = [
    {
        "chunk_size": 200,
        "overlap": 20,
        "top_k": 3
    },
    {
        "chunk_size": 500,
        "overlap": 50,
        "top_k": 5
    },
    {
        "chunk_size": 1000,
        "overlap": 100,
        "top_k": 5
    }
]

with open(EXP) as f:
    questions = json.load(f)

results = []

for config in configs:
    print("\nTesting:", config)

    rag = RAGPipeline(
        pdf__folder=PDF,
        chunk_overlap=config["overlap"],
        chunk_size=config["chunk_size"],
        top_k=config["top_k"],
        vector_db_path="./vector_db"
    )
    rag.build()

    for item in questions:
        answer = rag.ask(item["question"])

        results.append({
            "config": config,
            "question": item["question"],
            "answer": answer
        })

with open("results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Done")