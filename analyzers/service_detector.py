from pathlib import Path

def detect_services(repo_path):

    services = []

    for item in Path(repo_path).rglob("*"):

        if item.is_dir():

            has_dockerfile = (
                item / "Dockerfile"
            ).exists()

            has_package_json = (
                item / "package.json"
            ).exists()

            if has_dockerfile or has_package_json:
                services.append(item.name)

    return sorted(set(services))

# def detect_services(repo_path):

#     services = []

#     service_keywords = [
#         "auth-service",
#         "post-service",
#         "comment-service",
#         "frontend"
#     ]

#     for item in Path(repo_path).rglob("*"):

#         if item.is_dir():

#             directory_name = item.name.lower()

#             if directory_name == "services":
#                 continue

#             if directory_name in service_keywords:
#                 services.append(item.name)

#     return sorted(set(services))