import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class LLM:
    def __init__(self, model="gemini-3.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=api_key,
            temperature=0.2,
            max_tokens=500
        )

    def generate(self, prompt):
        messages = [
            (
                "system",
                "You are a helpful AI assistant. Answer ONLY using the provided context."
            ),
            (
                "user", 
                prompt
            ),
        ]
        
        response = self.client.invoke(messages)
        
        return response.content