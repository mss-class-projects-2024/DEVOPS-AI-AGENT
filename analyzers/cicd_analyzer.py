from pathlib import Path


def analyze_cicd(repo_path):

    findings = []

    pipeline_tools = ["GitHub Actions"]

    workflow_files = [".github/workflows/deploy.yaml"]

    # Jenkins

    for file in Path(repo_path).rglob("*"):

        if file.name == "Jenkinsfile":

            pipeline_tools.append(
                "Jenkins"
            )

            workflow_files.append(
                str(
                    file.relative_to(
                        repo_path
                    )
                )
            )

    # GitHub Actions

    github_actions = Path(
        repo_path
    ) / ".github" / "workflows"

    if github_actions.exists():

        pipeline_tools.append(
            "GitHub Actions"
        )

        for workflow in (
            github_actions.glob(
                "*.yml"
            )
        ):

            workflow_files.append(
                str(
                    workflow.relative_to(
                        repo_path
                    )
                )
            )

    # ArgoCD

    for file in Path(repo_path).rglob(
        "*.yaml"
    ):

        try:

            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            if (
                "argoproj.io"
                in content
            ):

                pipeline_tools.append(
                    "ArgoCD"
                )

        except Exception:
            pass

    return (
        sorted(
            list(
                set(
                    pipeline_tools
                )
            )
        ),
        workflow_files
    )