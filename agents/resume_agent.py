import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class ResumeAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def analyze(self, resume_text: str):
        prompt = f"""
        You are a professional resume reviewer.
        Give:
        - ATS friendliness feedback
        - Formatting issues
        - 5 concrete improvement suggestions
        Resume:
        {resume_text}
        """
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
