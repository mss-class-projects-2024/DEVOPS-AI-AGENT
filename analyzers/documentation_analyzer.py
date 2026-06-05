from pathlib import Path


IGNORE_DIRS = {
    "node_modules",
    ".git",
    "venv",
    "__pycache__",
    "dist",
    "build",
    ".terraform"
}


def analyze_documentation(repo_path):

    docs = []

    doc_files = {
        "README.md",
        "readme.md",
        "APP-SETUP.md",
        "INSTALL.md",
        "DEPLOYMENT.md",
        "ARCHITECTURE.md",
        "CONTRIBUTING.md"
    }

    for file in Path(repo_path).rglob("*"):

        # Skip unwanted directories
        if any(
            part in IGNORE_DIRS
            for part in file.parts
        ):
            continue

        if not file.is_file():
            continue

        if file.name not in doc_files:
            continue

        try:

            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            docs.append({
                "file": str(
                    file.relative_to(repo_path)
                ),
                "content": content[:5000]
            })

        except Exception:
            pass

    return docs