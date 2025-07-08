import json

def get_roadmap_for_role(role, roadmap_file="data/roadmaps.json"):
    with open(roadmap_file, "r") as f:
        data = json.load(f)

    for entry in data:
        if entry["job_role"].lower() == role.lower():
            return entry["roadmap"]

    return None
