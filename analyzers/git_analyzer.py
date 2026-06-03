from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    "dist",
    "build"
}


def scan_repository(repo_path):
    files = []

    for file in Path(repo_path).rglob("*"):

        # Skip ignored directories
        if any(ignore in file.parts for ignore in IGNORE_DIRS):
            continue

        if file.is_file():
            files.append(str(file))

    return files