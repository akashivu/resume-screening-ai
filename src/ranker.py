from src.extract_text import extract_text_from_pdf
from src.extract_text import clean_text
from src.similarity_engine import calculate_similarity
from src.skill_extractor import extract_skills
import os

def rank_resumes(resume_paths, job_description):

    ranked_resumes = []

    cleaned_job_description = clean_text(job_description)

    for resume_path in resume_paths:

        
        resume_text = extract_text_from_pdf(resume_path)

    
        cleaned_resume = clean_text(resume_text)

        
        score = calculate_similarity(
            cleaned_resume,
            cleaned_job_description
        )

        
        skills = extract_skills(cleaned_resume)

        ranked_resumes.append({

            "resume": os.path.basename(resume_path),

            "score": round(score, 2),

            "skills": skills

        })

    # Sort descending
    ranked_resumes.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked_resumes