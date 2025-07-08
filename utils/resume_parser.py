import docx2txt
import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

def extract_skills(text):
    text = text.lower()
    skill_keywords = [
        "python", "sql", "ml", "data analysis", "statistics", "tensorflow",
        "nlp", "html", "css", "react", "aws", "docker", "excel", "power bi"
    ]
    found_skills = [skill for skill in skill_keywords if skill in text]
    return ", ".join(found_skills)
