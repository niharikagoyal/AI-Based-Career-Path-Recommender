import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_roles(user_skills, job_data_path="data/job_roles.json"):
    with open(job_data_path, "r") as f:
        job_data = json.load(f)

    roles = [item["job_role"] for item in job_data]
    skills = [item["required_skills"] for item in job_data]

    vectorizer = TfidfVectorizer()
    skill_matrix = vectorizer.fit_transform(skills + [user_skills])

    cosine_sim = cosine_similarity(skill_matrix[-1], skill_matrix[:-1])
    scores = cosine_sim.flatten()

    top_indices = scores.argsort()[::-1][:3]
    return [roles[i] for i in top_indices]
