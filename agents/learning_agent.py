from groq import Groq
from config import GROQ_MODEL, get_groq_api_key
from dotenv import load_dotenv

load_dotenv()

class LearningAgent:
    def __init__(self):
        self.client = Groq(api_key=get_groq_api_key())

    def analyze(self, skill_gap_text: str):
        prompt = f"""
        You are a learning advisor.
        Based on this skill gap analysis, suggest:
        - Courses
        - Certifications
        - 3-month learning roadmap
        Skill Gap:
        {skill_gap_text}
        """
        response = self.client.chat.completions.create(
            model=GROQ_MODEL,

            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
