# RAG Knowledge Assistant (rag-knowledge-assistant)

This project is a comprehensive **RAG (Retrieval-Augmented Generation)** pipeline designed to read PDF files, split them into optimal chunks, convert them into vector embeddings, and store them locally using **FAISS**. Users can then ask natural language questions, and the system leverages **Google Gemini** to generate precise, technical answers grounded *only* in the retrieved PDF context.

## 🛠️ Tools & Tech Stack

* **Language:** Python 3.10+
* **LLM Engine:** `langchain-google-genai` (Google Gemini API via LangChain).
* **Embedding Model:** `sentence-transformers` for high-quality local text vectorization.
* **Orchestration:** `langchain` & `langchain-community` for prompt and pipeline management.
* **Vector Database:** `faiss-cpu` for ultra-fast similarity search.
* **PDF Loading:** `pypdf` for parsing and text extraction.
* **Text Splitting:** `langchain-text-splitters` for semantic text chunking.

---

## 📁 Generated Vector DB Artifacts

Once the pipeline processes your document structure, it creates a `vector_db` folder containing two essential files:

1. **`vector_db/index.faiss`**: Holds the mathematical dense vectors optimized for rapid search.
2. **`vector_db/metadata.pkl`**: A pickled file containing the actual text contents and page numbers corresponding to those vectors.

---

## 🚀 Setup & Execution Guide

Follow these steps to get the project up and running on your local machine:

### 1. Create and Activate the Virtual Environment

Open your terminal in the root project directory and run:

```bash
# Create virtual environment
python -m venv venv

# Activate environment (Windows)
.\venv\Scripts\activate

# Activate environment (Mac/Linux)
source venv/bin/activate

```

### 2. Install Dependencies

Install all the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt

```

### 3. Setup Environment Variables

Create a file named `.env` in the root directory of your project and insert your Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here

```

### 4. Add PDF Documents

Place all target PDF books or documents inside the designated folder path:
`../data/pdf_files/`

### 5. Run the Pipeline

Execute your main python script to build/load the database and query your assistant:

```bash
python main.py

```