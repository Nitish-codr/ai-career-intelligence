from agents.job_market_agent import JobMarketAgent
from agents.skill_gap_agent import SkillGapAgent
from agents.learning_agent import LearningAgent
from agents.resume_agent import ResumeAgent
from agents.ethics_agent import EthicsAgent
from analytics.scoring import calculate_score
from analytics.charts import generate_skill_chart

class CareerOrchestrator:
    def __init__(self):
        self.job_agent = JobMarketAgent()
        self.skill_agent = SkillGapAgent()
        self.learning_agent = LearningAgent()
        self.resume_agent = ResumeAgent()
        self.ethics_agent = EthicsAgent()

    def run(self, resume_text: str):
        job_market = self.job_agent.analyze(resume_text)
        skill_gap, skill_data = self.skill_agent.analyze(resume_text)
        learning = self.learning_agent.analyze(skill_gap)
        resume_feedback = self.resume_agent.analyze(resume_text)
        ethics = self.ethics_agent.analyze(resume_text)

        score = calculate_score(skill_data, resume_feedback)
        chart = generate_skill_chart(skill_data)

        return {
            "job_market": job_market,
            "skill_gap": skill_gap,
            "learning": learning,
            "resume": resume_feedback,
            "ethics": ethics,
            "score": score,
            "chart": chart
        }
