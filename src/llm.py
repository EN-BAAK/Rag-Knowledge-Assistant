import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLM:
    def __init__(self, model="gemini-3.5-flash"):
        self.client = OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = model

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistant. "
                        "Answer ONLY using the provided context."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=500
        )

        return response.choices[0].message.content