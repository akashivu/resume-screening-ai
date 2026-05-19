def generate_dashboard_metrics(ranked_resumes):

    total_resumes = len(ranked_resumes)

    average_score = 0

    top_candidate = "N/A"

    total_skills = 0

    if ranked_resumes:

        average_score = sum(
            resume["score"]
            for resume in ranked_resumes
        ) / total_resumes

        top_candidate = ranked_resumes[0]["resume"]

        all_skills = []

        for resume in ranked_resumes:

            all_skills.extend(resume["skills"])

        total_skills = len(set(all_skills))

    return {

        "total_resumes": total_resumes,

        "average_score": round(average_score, 2),

        "top_candidate": top_candidate,

        "total_skills": total_skills

    }