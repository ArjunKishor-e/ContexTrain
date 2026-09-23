import sys

from contextrain.indexer import index_project
from contextrain.memory import read_file


def main() -> None:
    project_path = sys.argv[1]

    files = index_project(project_path)

    print(f"Found {len(files)} files:\n")

    for file in files:
        print(f"--- {file.name} ---")

        content = read_file(file)
        print(content[:500])

        print()


if __name__ == "__main__":
    main()