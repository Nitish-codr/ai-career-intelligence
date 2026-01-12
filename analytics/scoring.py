def calculate_score(skill_data: dict, resume_feedback: str):
    base = sum(skill_data.values()) / (len(skill_data) * 10) * 100

    penalty = 0
    if "poor" in resume_feedback.lower():
        penalty = 10

    final_score = int(base - penalty)
    return max(0, min(final_score, 100))
