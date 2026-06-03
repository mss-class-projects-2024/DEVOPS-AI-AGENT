from pathlib import Path


def analyze_k8s(repo_path):

    findings = []

    for yaml_file in Path(repo_path).rglob("*.yaml"):

        content = yaml_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        relative_path = yaml_file.relative_to(
            repo_path
        )

        if "kind: Deployment" in content:

            if "readinessProbe" not in content:
                findings.append(
                    f"{relative_path}: Missing readinessProbe"
                )

            if "livenessProbe" not in content:
                findings.append(
                    f"{relative_path}: Missing livenessProbe"
                )

            if "resources:" not in content:
                findings.append(
                    f"{relative_path}: Missing resource limits/requests"
                )

            if ":latest" in content:
                findings.append(
                    f"{relative_path}: Using latest image tag"
                )

    return findings