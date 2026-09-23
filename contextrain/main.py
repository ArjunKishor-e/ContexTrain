import sys

from contextrain.indexer import index_project
from contextrain.memory import chunk_text, read_file


def main() -> None:
    project_path = sys.argv[1]

    files = index_project(project_path)

    for file in files:
        content = read_file(file)
        chunks = chunk_text(content)

        print(f"{file.name}: {len(chunks)} chunks")


if __name__ == "__main__":
    main()