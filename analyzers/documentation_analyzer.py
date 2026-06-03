from pathlib import Path


def analyze_documentation(repo_path):

    docs = []

    doc_files = [
        "README.md",
        "readme.md",
        "APP-SETUP.md",
        "INSTALL.md",
        "DEPLOYMENT.md",
        "ARCHITECTURE.md"
    ]

    for file in Path(repo_path).rglob("*"):

        if file.name in doc_files:

            try:

                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                docs.append({
                    "file": str(file),
                    "content": content[:5000]
                })

            except Exception:
                pass

    return docs