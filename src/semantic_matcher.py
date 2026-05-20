from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_similarity(
    resume_text,
    job_description
):

    # Generate embeddings
    resume_embedding = model.encode(
        [resume_text]
    )

    jd_embedding = model.encode(
        [job_description]
    )

    # Similarity
    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )

    return similarity[0][0] * 100