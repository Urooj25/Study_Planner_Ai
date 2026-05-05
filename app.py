import streamlit as st
from agent import generate_study_plan, save_to_history, load_history
from datetime import date
from pdf_generator import create_pdf
import os

# Page Config
st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="centered"
)

# Title
st.title("📚 AI Study Planner Agent")
st.markdown("*Your personal AI-powered study assistant!*")
st.divider()

# Tabs
tab1, tab2 = st.tabs(["📝 Create Plan", "📋 History"])

# ---- TAB 1: Create Plan ----
with tab1:
    st.subheader("Enter Your Study Details")

    subjects = st.text_input(
        "📖 Subjects (comma separated)",
        placeholder="Math, Physics, Chemistry"
    )

    weak_topics = st.text_area(
        "😟 Weak Topics (comma separated)",
        placeholder="Trigonometry, Thermodynamics, Organic Chemistry",
        help="Jin topics mein aap weak hain woh likho — AI unpar extra focus karega!"
    )

    exam_date = st.date_input(
        "📅 Exam Date",
        min_value=date.today()
    )

    hours_per_day = st.slider(
        "⏰ Study Hours Per Day",
        min_value=1,
        max_value=12,
        value=3
    )

    difficulty = st.selectbox(
        "🎯 Difficulty Level",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("🚀 Generate My Study Plan!", use_container_width=True):
        if not subjects:
            st.error("Please enter your subjects!")
        elif not weak_topics:
            st.error("Please enter your weak topics!")
        else:
            with st.spinner("AI is creating your personalized plan..."):
                plan = generate_study_plan(
                    subjects, weak_topics, exam_date, hours_per_day, difficulty
                )
                save_to_history(subjects, weak_topics, exam_date, plan)

            st.success("✅ Your Study Plan is Ready!")
            st.markdown(plan)

            # PDF Download Button
            st.divider()
            with st.spinner("PDF ban raha hai..."):
                pdf_path = create_pdf(
                    subjects, weak_topics, exam_date, hours_per_day, difficulty, plan
                )

            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download PDF",
                    data=f,
                    file_name="study_plan.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

# ---- TAB 2: History ----
with tab2:
    st.subheader("📋 Your Previous Study Plans")

    history = load_history()

    if not history:
        st.info("No plans yet! Create your first plan.")
    else:
        for i, entry in enumerate(reversed(history)):
            with st.expander(
                f"📅 {entry['date']} — Subjects: {entry['subjects']}"
            ):
                st.markdown(f"**😟 Weak Topics:** {entry.get('weak_topics', 'N/A')}")
                st.divider()
                st.markdown(entry["plan"])



