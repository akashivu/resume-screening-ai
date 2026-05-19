def compare_skills(resume_skills, job_skills):

    resume_skills_set = set(
        skill.lower() for skill in resume_skills
    )

    job_skills_set = set(
        skill.lower() for skill in job_skills
    )

    matched_skills = list(
        resume_skills_set.intersection(job_skills_set)
    )

    missing_skills = list(
        job_skills_set.difference(resume_skills_set)
    )

    return matched_skills, missing_skills