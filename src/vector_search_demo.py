from src.vector_store import (
    add_resume_to_index,
    search_resumes
)


# Add sample resumes to vector index
add_resume_to_index(
    "resume1.pdf",
    "Python Flask Machine Learning SQL"
)

add_resume_to_index(
    "resume2.pdf",
    "React Frontend JavaScript CSS"
)

add_resume_to_index(
    "resume3.pdf",
    "AWS Docker Kubernetes DevOps"
)


# Perform semantic search
results = search_resumes(
    "Looking for Python backend engineer"
)


# Print retrieved resumes
print(results)