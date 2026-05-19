from src.extract_text import extract_text_from_pdf
from src.extract_text import clean_text

from src.similarity_engine import calculate_similarity
from src.skill_extractor import extract_skills
from src.skill_matcher import compare_skills

import os


def rank_resumes(resume_paths, job_description):

    ranked_resumes = []

    # Clean job description
    cleaned_job_description = clean_text(job_description)

    # Extract job skills
    job_skills = extract_skills(cleaned_job_description)

    for resume_path in resume_paths:

        # Extract text
        resume_text = extract_text_from_pdf(resume_path)

        # Clean resume
        cleaned_resume = clean_text(resume_text)

        # Similarity score
        score = calculate_similarity(
            cleaned_resume,
            cleaned_job_description
        )

        # Extract resume skills
        resume_skills = extract_skills(cleaned_resume)

        # Compare skills
        matched_skills, missing_skills = compare_skills(
            resume_skills,
            job_skills
        )

        ranked_resumes.append({

            "resume": os.path.basename(resume_path),

            "score": round(score, 2),

            "skills": resume_skills,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills

        })

    # Sort by highest score
    ranked_resumes.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked_resumes