import sys

from contextrain.indexer import index_project
from contextrain.llm import generate_answer
from contextrain.memory import chunk_text, read_file
from contextrain.search import search_chunks


def main() -> None:
    project_path = sys.argv[1]

    files = index_project(project_path)

    all_chunks = []

    for file in files:
        content = read_file(file)
        chunks = chunk_text(content)
        all_chunks.extend(chunks)

    query = "Where does the application handle API routes?"

    relevant_chunks = search_chunks(query, all_chunks)

    answer = generate_answer(query, relevant_chunks)

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()