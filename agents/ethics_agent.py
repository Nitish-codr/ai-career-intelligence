from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL
from dotenv import load_dotenv

load_dotenv()

class EthicsAgent:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)


    def analyze(self, resume_text: str):
        prompt = f"""
        You are an AI ethics auditor.
        Check the resume analysis for:
        - Bias
        - Fairness
        - Gender or socio-economic assumptions
        Give ethical recommendations.
        Resume:
        {resume_text}
        """
        response = self.client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
