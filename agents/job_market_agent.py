from groq import Groq
from config import GROQ_MODEL, get_groq_api_key
from dotenv import load_dotenv

load_dotenv()

class JobMarketAgent:
    def __init__(self):
        self.client = Groq(api_key=get_groq_api_key())

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
            model=GROQ_MODEL,

            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
