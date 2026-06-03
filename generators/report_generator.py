from pathlib import Path


def generate_report(
    repo_path,
    technologies,
    project_type,
    project_structure,
    services,
    dependencies,
    k8s_findings,
    docker_findings,
    terraform_findings
):

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "project_report.md"

    with open(report_file, "w", encoding="utf-8") as f:

        f.write("# Project Analysis Report\n\n")

        f.write("## Project Type\n")
        f.write(f"{project_type}\n\n")

        f.write("## Technologies\n")
        for tech in technologies:
            f.write(f"- {tech}\n")

        f.write("\n## Structure\n")
        for item in project_structure:
            f.write(f"- {item}\n")

        f.write("\n## Services\n")
        for service in services:
            f.write(f"- {service}\n")

        f.write("\n## Required Tools\n")
        for dep in dependencies:
            f.write(f"- {dep}\n")

        f.write("\n## Kubernetes Findings\n")
        if k8s_findings:
            for finding in k8s_findings:
                f.write(f"- {finding}\n")
        else:
            f.write("No issues detected\n")

        f.write("\n## Docker Findings\n")
        if docker_findings:
            for finding in docker_findings:
                f.write(f"- {finding}\n")
        else:
            f.write("No issues detected\n")

        f.write("\n## Terraform Findings\n")
        if terraform_findings:
            for finding in terraform_findings:
                f.write(f"- {finding}\n")
        else:
            f.write("No issues detected\n")

    return report_file