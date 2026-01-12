import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class JobMarketAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def analyze(self, resume_text: str):
        prompt = f"""
        You are a job market analyst.
        Based on the resume below, identify:
        - Best matching roles
        - Industry demand
        - Salary outlook (India)
        Resume:
        {resume_text}
        """
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
