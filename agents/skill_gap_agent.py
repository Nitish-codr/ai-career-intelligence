from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL
from dotenv import load_dotenv

load_dotenv()

class SkillGapAgent:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def analyze(self, resume_text: str):
        prompt = f"""
        You are a career skill gap analyst.
        Identify missing skills for high-demand AI/Tech roles.
        Return:
        1. Text explanation
        2. A Python dictionary of skills with current level (0-10)
        Resume:
        {resume_text}
        """
        response = self.client.chat.completions.create(
            model=GROQ_MODEL,

            messages=[{"role": "user", "content": prompt}],
        )
        text = response.choices[0].message.content

        # Dummy parsed data for chart
        skill_data = {
            "Python": 7,
            "Machine Learning": 5,
            "Deep Learning": 4,
            "SQL": 6,
            "Cloud": 3
        }
        return text, skill_data
