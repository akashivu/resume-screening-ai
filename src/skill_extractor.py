import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [

    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "flask",
    "django",
    "react",
    "spring boot",
    "sql",
    "mongodb",
    "docker",
    "kubernetes",
    "aws",
    "git",
    "github",
    "html",
    "css",
    "javascript",
    "tensorflow",
    "pandas",
    "numpy",
    "scikit-learn"

]


def extract_skills(text):

    doc = nlp(text.lower())

    found_skills = set()

    for token in doc:

        if token.text in SKILLS:
            found_skills.add(token.text)

    # Handle multi-word skills
    for skill in SKILLS:

        if skill in text.lower():
            found_skills.add(skill)

    return list(found_skills)