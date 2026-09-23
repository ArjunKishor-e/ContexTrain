from pathlib import Path


def read_file(file_path: Path) -> str:
    """Read a text file and return its contents."""

    return file_path.read_text(encoding="utf-8")