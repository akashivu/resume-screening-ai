from flask import Flask, render_template, request
import os

from src.extract_text import extract_text_from_pdf
from src.extract_text import clean_text

from src.similarity_engine import calculate_similarity
from src.skill_extractor import extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    uploaded_file = request.files["resume"]

    job_description = request.form["job_description"]


    if uploaded_file:

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            uploaded_file.filename
        )

        uploaded_file.save(file_path)


        # Extract Resume Text
        resume_text = extract_text_from_pdf(file_path)


        # Clean Resume Text
        resume_text = clean_text(resume_text)


        # Clean Job Description
        job_description = clean_text(job_description)
       
        resume_skills = extract_skills(resume_text)

        job_skills = extract_skills(job_description)

        # Calculate Similarity
        match_percentage = calculate_similarity(
            resume_text,
            job_description
        )


        return render_template(
            "index.html",
            match=f"{match_percentage:.2f}",
            resume_skills=resume_skills,
            job_skills=job_skills

        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)