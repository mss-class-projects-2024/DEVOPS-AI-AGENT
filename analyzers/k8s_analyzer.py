from pathlib import Path
import yaml


def analyze_k8s(repo_path):

    findings = []

    for yaml_file in Path(repo_path).rglob("*.yaml"):

        try:

            with open(yaml_file, "r", encoding="utf-8") as f:

                docs = list(yaml.safe_load_all(f))

            for doc in docs:

                if not isinstance(doc, dict):
                    continue

                kind = doc.get("kind")

                relative_path = yaml_file.relative_to(
                    repo_path
                )

                if kind != "Deployment":
                    continue

                content = yaml.dump(doc)

                if "readinessProbe" not in content:
                    findings.append(
                        f"{relative_path}: Missing readinessProbe"
                    )

                if "livenessProbe" not in content:
                    findings.append(
                        f"{relative_path}: Missing livenessProbe"
                    )

                if "resources" not in content:
                    findings.append(
                        f"{relative_path}: Missing resource limits/requests"
                    )

                if ":latest" in content:
                    findings.append(
                        f"{relative_path}: Using latest image tag"
                    )

        except Exception:
            pass

    return findings