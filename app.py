from flask import Flask, render_template, request
import os

os.makedirs("uploads", exist_ok=True)
from src.extract_text import extract_text_from_pdf
from src.extract_text import clean_text

from src.similarity_engine import calculate_similarity
from src.skill_extractor import extract_skills

from src.ranker import rank_resumes

from src.dashboard_metrics import generate_dashboard_metrics

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    uploaded_files = request.files.getlist("resume")

    job_description = request.form["job_description"]

    saved_paths = []

    for file in uploaded_files:

        if file:

            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(file_path)

            saved_paths.append(file_path)

    ranked_resumes = rank_resumes(
        saved_paths,
        job_description
    )
    dashboard_metrics = generate_dashboard_metrics(
    ranked_resumes
    )
    return render_template(
        "index.html",
        ranked_resumes=ranked_resumes,
        dashboard_metrics=dashboard_metrics

    )


if __name__ == "__main__":
    app.run(debug=True)