import streamlit as st
from orchestrator import CareerOrchestrator
from utils.resume_reader import read_resume_text

st.set_page_config(page_title="AI Career Intelligence", layout="wide")

st.title("🎯 AI Career Intelligence Platform")
st.write("Multi-Agent System for Employability, Skill Gap & Ethical AI Guidance")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading resume..."):
        resume_text = read_resume_text(uploaded_file)

    st.subheader("📄 Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=200)

    if st.button("🔍 Analyze My Career"):
        with st.spinner("Running AI Agents..."):
            orchestrator = CareerOrchestrator()
            results = orchestrator.run(resume_text)

        st.success("Analysis Completed!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📈 Job Market Intelligence")
            st.write(results["job_market"])

            st.subheader("🧠 Learning Recommendations")
            st.write(results["learning"])

            st.subheader("⚖️ Ethics & Fairness Check")
            st.write(results["ethics"])

        with col2:
            st.subheader("🧩 Skill Gap Analysis")
            st.write(results["skill_gap"])

            st.subheader("📄 Resume Feedback")
            st.write(results["resume"])

            st.subheader("📊 Employability Score")
            st.metric("Score", f'{results["score"]}/100')

        st.subheader("📉 Skill Gap Visualization")
        st.pyplot(results["chart"])
