import matplotlib.pyplot as plt

def generate_skill_chart(skill_data: dict):
    skills = list(skill_data.keys())
    values = list(skill_data.values())

    fig, ax = plt.subplots()
    ax.bar(skills, values)
    ax.set_ylim(0, 10)
    ax.set_title("Skill Gap Overview")
    ax.set_ylabel("Skill Level (0-10)")
    return fig
