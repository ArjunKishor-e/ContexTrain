import ollama


def generate_answer(question: str, context: list[str]) -> str:
    """Generate an answer using the provided project context."""

    context_text = "\n\n".join(context)

    prompt = f"""
Use the provided project context as the source of truth.

If the context contains code that directly answers the question, state that answer directly.

For example, if the context shows a model name, library, function, file, or configuration value, use that information in your answer.

Only say "I don't know based on the provided project context." when the required information genuinely does not appear anywhere in the provided context.

Do not invent information that is not present in the context.

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