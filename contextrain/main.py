import sys

from contextrain.indexer import index_project
from contextrain.memory import get_project_summary


def main() -> None:
    project_path = sys.argv[1]

    files = index_project(project_path)

    summary = get_project_summary(files)

    print(summary)


if __name__ == "__main__":
    main()