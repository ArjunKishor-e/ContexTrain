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


def chunk_text(text: str, chunk_size: int = 50) -> list[str]:
    """Split text into chunks of lines."""

    lines = text.splitlines()

    chunks = []

    for i in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[i:i + chunk_size])
        chunks.append(chunk)

    return chunks