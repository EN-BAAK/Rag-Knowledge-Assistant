from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            documents.append(
                {
                    "page": page_number + 1,
                    "text": text,
                }
            )

    return documents

"""
[
    {
    page:1,
    text:"..."
    },

    {
    page:2,
    text:"..."
    }
]
"""