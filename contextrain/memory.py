from pathlib import Path


def read_file(file_path: Path) -> str:
    """Read a text file and return its contents."""

    return file_path.read_text(encoding="utf-8")


def get_project_summary(files: list[Path]) -> str:
    """Create a basic summary of the project files."""

    summary = []

    summary.append(f"Total files: {len(files)}")
    summary.append("")
    summary.append("Files:")

    for file in files:
        summary.append(f"- {file}")

    return "\n".join(summary)