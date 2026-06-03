from pathlib import Path
import re


def analyze_docker(repo_path):

    findings = []

    # Dockerfile Checks
    for dockerfile in Path(repo_path).rglob("Dockerfile"):

        content = dockerfile.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        relative_path = dockerfile.relative_to(
            repo_path
        )

        if "HEALTHCHECK" not in content:
            findings.append(
                f"{relative_path}: Missing HEALTHCHECK"
            )

        if "USER " not in content:
            findings.append(
                f"{relative_path}: Running as root user"
            )

        if ":latest" in content:
            findings.append(
                f"{relative_path}: Using latest base image"
            )

    # Docker Compose Checks
    compose_files = list(
        Path(repo_path).rglob("docker-compose*.y*ml")
    )

    for compose_file in compose_files:

        content = compose_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        relative_path = compose_file.relative_to(
            repo_path
        )

        if "restart:" not in content:

            findings.append(
                f"{relative_path}: Missing restart policy"
            )

        if re.search(
            r'PASSWORD\s*[:=]',
            content,
            re.IGNORECASE
        ):

            findings.append(
                f"{relative_path}: Possible hardcoded password"
            )

        if ":latest" in content:

            findings.append(
                f"{relative_path}: Using latest image tag"
            )

    return findings