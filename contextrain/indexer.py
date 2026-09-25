from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode",
}

IGNORED_FILES = {
    ".gitignore",
    ".env",
    ".env.local",
    ".env.development",
    ".env.production",
}


def index_project(project_path: str) -> list[Path]:
    """Return source files found inside a project."""

    root = Path(project_path).resolve()

    if not root.exists():
        raise FileNotFoundError(f"Project not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    files = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if path.name in IGNORED_FILES:
            continue

        if any(part in IGNORED_DIRECTORIES for part in path.parts):
            continue

        files.append(path)

    return sorted(files)