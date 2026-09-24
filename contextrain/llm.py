import ollama


def generate_answer(question: str, context: list[str]) -> str:
    """Generate an answer using the provided project context."""

    context_text = "\n\n".join(context)

    prompt = f"""
Answer the question using the project context below.

If the answer cannot be found in the context, say:
"I don't know based on the provided project context."

Do not make assumptions or invent files, functions, or directories.

Project context:
{context_text}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]