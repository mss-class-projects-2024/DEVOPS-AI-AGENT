import os


IGNORE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    "dist",
    "build",
    "coverage",
    ".terraform",
    ".idea",
    ".vscode"
}


SERVICE_KEYWORDS = [
    "service",
    "api",
    "backend",
    "frontend",
    "gateway"
]


def detect_services(repo_path):

    services = set()

    for root, dirs, files in os.walk(repo_path):

        # Ignore unwanted directories
        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        folder_name = os.path.basename(root).lower()

        # Detect service folders
        for keyword in SERVICE_KEYWORDS:

            if keyword in folder_name:

                services.add(
                    os.path.basename(root)
                )

                break

        # Detect Dockerized services
        if "Dockerfile" in files:

            parent = os.path.basename(root)

            if parent.lower() not in {
                "docker",
                "containers"
            }:

                services.add(parent)

    return sorted(list(services))