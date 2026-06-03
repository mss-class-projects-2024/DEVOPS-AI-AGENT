from pathlib import Path


def analyze_structure(repo_path):

    directories = []

    root = Path(repo_path)

    for item in root.iterdir():

        if item.is_dir():

            if item.name.startswith("."):
                continue

            directories.append(item.name)

    return sorted(directories)