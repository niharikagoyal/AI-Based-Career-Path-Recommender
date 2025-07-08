import json
import spacy

# Load SpaCy's medium English model (you must download it first)
nlp = spacy.load("en_core_web_md")

def recommend_roles_spacy(user_skills, job_data_path="data/job_roles.json"):
    with open(job_data_path, "r") as f:
        job_data = json.load(f)

    roles = [item["job_role"] for item in job_data]
    skills = [item["required_skills"] for item in job_data]

    user_doc = nlp(user_skills)
    scores = []

    for role_skills in skills:
        role_doc = nlp(role_skills)
        similarity = user_doc.similarity(role_doc)
        scores.append(similarity)

    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]
    return [roles[i] for i in top_indices]
