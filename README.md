# 🧠 AI Career Path Recommender

An AI-powered web application that recommends personalized career paths, identifies skill gaps, suggests relevant courses, and provides step-by-step learning roadmaps — all based on your skills or uploaded resume.

## 🌟 Features

- 📝 **Skill Input Options**: Enter your skills manually or upload a resume (PDF/DOCX) for auto extraction using NLP.
- 🎯 **AI-Based Career Recommendations**: Find roles that best match your current capabilities using `spaCy`.
- 🧠 **Skill Gap Analysis**: Discover missing skills required for your ideal job roles.
- 🎓 **Course Suggestions**: Get curated online courses (Coursera, Udemy, etc.) to fill skill gaps.
- 🧭 **Learning Roadmaps**: Structured paths to help you grow into recommended roles.

## 📁 Project Structure

AI_Career_Path_Recommender/
├── app.py
├── requirements.txt
├── packages.txt
├── data/
│ ├── job_roles.json
│ ├── courses.json
│ └── roadmaps.json
└── utils/
├── recommend_roles_spacy.py
├── recommender.py
├── resume_parser.py
├── roadmap.py
└── skill_gap.py

## ⚙️ Tech Stack
Backend: Python, spaCy, scikit-learn, PyMuPDF, docx2txt, pandas, json
Frontend: Streamlit

## ⚙️Getting Started

1. 🧾 Clone the Repository
   git clone <https://github.com/niharikagoyal/AI-Based-Career-Path-Recommender.git>
   cd AI_Career_Path_Recommender
2. 📦 Install Python Dependencies
   pip install -r requirements.txt
3. 📥 Download spaCy Model
   python -m spacy download en_core_web_md
4. ▶️ Run the App
   streamlit run app.py
   
## 🧪 How to Use

-Choose to enter skills manually or upload a resume.

-Click “🚀 Recommend Career Paths”.

-View recommended roles, skill gaps, courses, and roadmaps.

## 📚 Data Files

-data/job_roles.json – Job roles & required skills

-data/courses.json – Courses for skills

-data/roadmaps.json – Roadmaps for career growth

## 🧠 Key Modules

-app.py – Streamlit frontend

-utils/recommend_roles_spacy.py – NLP role recommendation

-utils/skill_gap.py – Skill gap checker and course suggester

-utils/roadmap.py – Roadmap for learning

-utils/resume_parser.py – Extract skills from PDF/DOCX

## 🎨 UI Features
-Responsive layout with sidebar controls

-Collapsible skill input and expandable sections

-Tabbed interface for recommendation, skill gaps, and roadmap

-Light/dark theme compatible

## 👩‍💼 Author
Niharika Goyal
BTech CSE | Data Scientist | Python & ML Developer

## 📄 License
MIT License – Free to use and modify for personal, academic, or commercial projects.
