from pathlib import Path


def generate_report(
    repo_path,
    technologies,
    project_type,
    project_structure,
    services,
    dependencies,
    databases,
    database_findings,
    project_dependencies,
    documentation,
    k8s_findings,
    docker_findings,
    terraform_findings,
    pipeline_tools,
    workflow_files,
    recommendations
):

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "project_report.md"

    with open(report_file, "w", encoding="utf-8") as f:

        f.write("# Project Analysis Report\n\n")

        f.write(f"Repository: {repo_path}\n\n")

        # Project Type
        f.write("## Project Type\n")
        f.write(f"{project_type}\n\n")

        # Technologies
        f.write("## Technologies\n")

        if technologies:
            for tech in sorted(technologies):
                f.write(f"- {tech}\n")
        else:
            f.write("No technologies detected\n")

        # Structure
        f.write("\n## Project Structure\n")

        if project_structure:
            for item in project_structure:
                f.write(f"- {item}\n")
        else:
            f.write("No structure detected\n")

        # Services
        f.write("\n## Services\n")

        if services:
            for service in services:
                f.write(f"- {service}\n")
        else:
            f.write("No services detected\n")

        # Required Tools
        f.write("\n## Required Tools\n")

        if dependencies:
            for dep in dependencies:
                f.write(f"- {dep}\n")
        else:
            f.write("No required tools detected\n")

        # Databases
        f.write("\n## Databases\n")

        if databases:
            for db in databases:
                f.write(f"- {db}\n")
        else:
            f.write("No databases detected\n")

        # Database Findings
        f.write("\n## Database Findings\n")

        if database_findings:
            for finding in database_findings:
                f.write(f"- {finding}\n")
        else:
            f.write("No database findings\n")

        # Project Dependencies
        f.write("\n## Project Dependencies\n")

        if project_dependencies:

            for file, deps in project_dependencies.items():

                f.write(f"\n### {file}\n")

                if deps.get("dependencies"):

                    f.write("\nDependencies:\n")

                    for dep in deps["dependencies"]:
                        f.write(f"- {dep}\n")

                if deps.get("devDependencies"):

                    f.write("\nDev Dependencies:\n")

                    for dep in deps["devDependencies"]:
                        f.write(f"- {dep}\n")

        else:
            f.write("No package dependencies found\n")

        # Documentation
        f.write("\n## Documentation Files\n")

        if documentation:

            for doc in documentation:

                file_name = doc.get(
                    "file",
                    "Unknown File"
                )

                content = (
                    doc.get("content")
                    or ""
                )

                f.write(
                    f"\n### {file_name}\n"
                )

                f.write(
                    content[:500]
                )

                f.write("\n\n")
        else:
            f.write(
                "No documentation files found\n"
            )

        # Kubernetes Findings
        f.write("\n## Kubernetes Findings\n")

        if k8s_findings:
            for finding in k8s_findings:
                f.write(f"- {finding}\n")
        else:
            f.write("No issues detected\n")

        # Docker Findings
        f.write("\n## Docker Findings\n")

        if docker_findings:
            for finding in docker_findings:
                f.write(f"- {finding}\n")
        else:
            f.write("No issues detected\n")

        # Terraform Findings
        f.write("\n## Terraform Findings\n")

        if terraform_findings:
            for finding in terraform_findings:
                f.write(f"- {finding}\n")
        else:
            f.write("No issues detected\n")

        # CI/CD Analysis
        f.write("\n## CI/CD Analysis\n")

        if pipeline_tools:

            f.write("\n### Pipeline Tools\n")

            for tool in pipeline_tools:
                f.write(f"- {tool}\n")

            f.write("\n### Workflow Files\n")

            if workflow_files:

                for file in workflow_files:
                    f.write(f"- {file}\n")

            else:
                f.write(
                    "No workflow files detected\n"
                )

        else:
            f.write(
                "No CI/CD pipeline detected\n"
            )

        # Recommendations
        f.write("\n## Recommendations\n")

        if recommendations:

            for recommendation in recommendations:

                f.write(
                    f"- {recommendation}\n"
                )

        else:

            f.write(
                "No recommendations generated\n"
            )
    return str(report_file)