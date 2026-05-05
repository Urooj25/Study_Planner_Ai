# 📚 AI Study Planner

An AI-powered study planning agent that creates personalized study plans based on your subjects, weak topics, and exam date.

## 🚀 Features
- Personalized daily study schedule
- Weak topic analysis & improvement tips
- Topic-wise tips & tricks
- Practice questions
- PDF download of study plan
- History of previous plans

## 🛠️ Tech Stack
- Streamlit (UI)
- Groq API - LLaMA 3.3 70B (AI)
- ReportLab (PDF Generation)
- Python

## ⚙️ Setup Instructions
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Create .env file:
   GROQ_API_KEY=your_key_here
4. Run the app:
   streamlit run app.py

## 🤖 AI Pipeline
Input (subjects + weak topics) → Groq LLaMA API → Study Plan → PDF Export
