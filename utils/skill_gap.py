import json

def get_missing_skills(user_skills: str, role_skills: str):
    user_set = set([s.strip().lower() for s in user_skills.split(",")])
    role_set = set([s.strip().lower() for s in role_skills.split(",")])
    return list(role_set - user_set)

def suggest_courses(missing_skills, course_data_path="data/courses.json"):
    import json
    with open(course_data_path, "r") as f:
        course_data = json.load(f)

    suggestions = []
    for skill in missing_skills:
        for course in course_data:
            if skill.strip().lower() == course["skill"].strip().lower():
                suggestions.append(course)
    return suggestions
