import json
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


def detect_project_dependencies(repo_path):

    dependencies = {}

    for package_file in Path(repo_path).rglob("package.json"):

        # Skip node_modules and other ignored directories
        if any(
            part in IGNORE_DIRS
            for part in package_file.parts
        ):
            continue

        try:

            with open(
                package_file,
                "r",
                encoding="utf-8"
            ) as f:

                package_data = json.load(f)

            relative_path = package_file.relative_to(
                repo_path
            )

            dependencies[
                str(relative_path)
            ] = {

                "dependencies":
                    list(
                        package_data.get(
                            "dependencies",
                            {}
                        ).keys()
                    ),

                "devDependencies":
                    list(
                        package_data.get(
                            "devDependencies",
                            {}
                        ).keys()
                    )
            }

        except Exception:
            pass

    return dependencies