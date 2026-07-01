from pathlib import Path
from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            documents.append(
                {
                    "source": file_path.name,
                    "page": page_number + 1,
                    "text": text,
                }
            )

    return documents

def load_all_pdfs(folder_path):
    folder = Path(folder_path)
    all_documents = []

    for pdf_file in folder.glob("*.pdf"):
        print(f"Loading: {pdf_file.name}")
        documents = load_pdf(pdf_file)

        all_documents.extend(documents)


    return all_documents

"""
[
    {
    "source":"attention.pdf",
    page:1,
    text:"..."
    },

    {
    "source":"attention.pdf",
    page:2,
    text:"..."
    }
]
"""