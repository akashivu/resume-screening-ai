import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


# Embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Vector dimension
dimension = 384

# FAISS index
index = faiss.IndexFlatL2(dimension)

# Metadata store
resume_metadata = []


def add_resume_to_index(
    resume_name,
    resume_text
):

    embedding = model.encode(
        [resume_text]
    )

    embedding = np.array(
        embedding,
        dtype="float32"
    )

    index.add(embedding)

    resume_metadata.append({

        "resume_name": resume_name,

        "text": resume_text

    })


def search_resumes(
    job_description,
    top_k=3
):

    query_embedding = model.encode(
        [job_description]
    )

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(resume_metadata):

            results.append(
                resume_metadata[idx]
            )

    return results