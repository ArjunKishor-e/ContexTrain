from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def search_chunks(query: str, chunks: list[str], top_k: int = 5) -> list[str]:
    """Return the most relevant chunks for a query."""

    chunk_embeddings = model.encode(chunks)
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]

    ranked_chunks = sorted(
        zip(chunks, similarities),
        key=lambda item: item[1],
        reverse=True,
    )

    return [chunk for chunk, score in ranked_chunks[:top_k]]