import streamlit as st
from utils.resume_parser import extract_text_from_pdf, extract_text_from_docx, extract_skills
from utils.recommend_roles_spacy import recommend_roles_spacy
from utils.skill_gap import get_missing_skills, suggest_courses
from utils.roadmap import get_roadmap_for_role
import json

# 🎨 Page config
st.set_page_config(page_title="AI Career Path Recommender", layout="wide")

# 🌟 Title
st.markdown("<h1 style='text-align: center; color: white;'>🧠 AI-Based Career Path Recommender</h1>", unsafe_allow_html=True)
st.markdown("---")

# 🧭 Sidebar Input Section
st.sidebar.title("🎯 Choose Input Method")
option = st.sidebar.radio("", ["📝 Enter Skills Manually", "📄 Upload Resume"])

user_skills = ""

# 📥 Input Section
with st.expander("📥 Provide Your Skills", expanded=True):
    if option == "📝 Enter Skills Manually":
        user_skills = st.text_input("💬 Enter your skills (comma-separated):")
    elif option == "📄 Upload Resume":
        uploaded_file = st.file_uploader("📎 Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
        if uploaded_file:
            if uploaded_file.name.endswith(".pdf"):
                text = extract_text_from_pdf(uploaded_file)
            else:
                text = extract_text_from_docx(uploaded_file)
            user_skills = extract_skills(text)
            st.success(f"✅ Extracted Skills: {user_skills}")

# 🚀 Career Recommendation
if st.button("🚀 Recommend Career Paths"):
    if user_skills:
        recommendations = recommend_roles_spacy(user_skills)
        top_role = recommendations[0]

        tabs = st.tabs(["🎯 Career Recommendations", "🧠 Skill Gap & Courses", "🧭 Learning Roadmap"])

        # Tab 1: Recommendations (clean version)
        with tabs[0]:
            st.subheader("🎯 Top Career Path Suggestions")
            st.markdown("Here are the career paths that align with your current skillset:")
            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"- **{i}. {rec}**")

        # Tab 2: Skill Gaps & Courses
        with tabs[1]:
            with open("data/job_roles.json") as f:
                job_data = json.load(f)
                selected_role_data = next(item for item in job_data if item["job_role"] == top_role)
                role_skills = selected_role_data["required_skills"]
                missing = get_missing_skills(user_skills, role_skills)

            if missing:
                st.subheader("🧠 Skill Gaps")
                st.write(", ".join(missing))

                st.subheader("🎓 Suggested Courses")
                for item in suggest_courses(missing):
                    st.markdown(f"<h4 style='margin-bottom:5px;'>{item['skill'].capitalize()}</h4>", unsafe_allow_html=True)
                    for course in item["courses"]:
                        st.markdown(f"- **{course['course']}** by {course['provider']} → [Go to Course]({course['link']})")
            else:
                st.success("✅ You already match all required skills for this role!")

        # Tab 3: Roadmap
        with tabs[2]:
            st.subheader("🧭 Learning Roadmap")
            roadmap = get_roadmap_for_role(top_role)
            if roadmap:
                for level, steps in roadmap.items():
                    st.markdown(f"<h5 style='color:#1E88E5'>{level}</h5>", unsafe_allow_html=True)
                    for step in steps:
                        st.markdown(f"- {step}")
            else:
                st.warning("No roadmap found for this role yet.")
    else:
        st.warning("⚠️ Please provide your skills or upload a resume.")
