from analyzers.git_analyzer import scan_repository
from analyzers.github_analyzer import clone_repository, cleanup_repository
from analyzers.technology_detector import detect_technologies
from analyzers.project_classifier import classify_project
from analyzers.dependency_detector import detect_dependencies
from analyzers.environment_validator import validate_environment
from analyzers.project_structure import analyze_structure
from analyzers.service_detector import detect_services
from analyzers.dependency_scanner import detect_project_dependencies
from analyzers.k8s_analyzer import analyze_k8s
from analyzers.docker_analyzer import analyze_docker
from analyzers.terraform_analyzer import analyze_terraform
from generators.report_generator import generate_report
from generators.architecture_generator import generate_architecture
from generators.setup_guide_generator import generate_setup_guide
from generators.troubleshooting_guide_generator import generate_troubleshooting_guide
from generators.interview_question_generator import generate_interview_questions
from analyzers.cicd_analyzer import analyze_cicd
from ai.repository_explainer import explain_repository
from ai.deployment_explainer import explain_deployment
from analyzers.documentation_analyzer import analyze_documentation


def main():

    repo_input = input(
        "Enter local path or Git URL: "
    ).strip()

    is_git_repo = (
        repo_input.startswith("http://")
        or repo_input.startswith("https://")
    )

    repo_path = None

    try:

        if is_git_repo:
            repo_path = clone_repository(repo_input)
        else:
            repo_path = repo_input

        files = scan_repository(repo_path)

        technologies = detect_technologies(files)

        dependencies = detect_dependencies(
            technologies
        )

        environment_status = (
            validate_environment(
                dependencies
            )
        )

        project_type = (
            classify_project(
                technologies
            )
        )

        project_structure = (
            analyze_structure(
                repo_path
            )
        )

        services = detect_services(
            repo_path
        )

        # Dependency Analysis

        project_dependencies = (
            detect_project_dependencies(
                repo_path
            )
        )
        # Documentation Analysis
        documentation = (
            analyze_documentation(
                repo_path
            )
        )

        k8s_findings = analyze_k8s(
            repo_path
        )

        docker_findings = (
            analyze_docker(
                repo_path
            )
        )

        # Terraform Analysis
        terraform_findings, terraform_components = (
            analyze_terraform(
                repo_path
            )
        )

        # CI/CD Analysis
        pipeline_tools, workflow_files = (
            analyze_cicd(
                repo_path
            )
        )

        # Architecture Generation
        architecture = (
            generate_architecture(
                project_type,
                services,
                terraform_components
            )
        )

        # Setup Guide Generation
        setup_guide = (
            generate_setup_guide(
                technologies,
                dependencies,
                services,
                terraform_components
            )
        )

        # Troubleshooting Guide Generation
        troubleshooting_guide = (
            generate_troubleshooting_guide(
                k8s_findings,
                docker_findings,
                terraform_findings
            )
        )

        # Interview Question Generation
        interview_questions = (
            generate_interview_questions(
                technologies,
                services,
                terraform_components
            )
        )

        # Report Generation
        report_file = generate_report(
            repo_path,
            technologies,
            project_type,
            project_structure,
            services,
            dependencies,
            k8s_findings,
            docker_findings,
            terraform_findings
        )

        # Repository Explanation
        with open(
            report_file,
            "r",
            encoding="utf-8"
        ) as f:

            report_text = f.read()

        documentation_text = ""

        for doc in documentation:

            documentation_text += (
                f"\n\nFILE: {doc['file']}\n"
            )

            documentation_text += (
                doc['content']
            )

        # Explain Repository using LLM
        ai_summary = (
            explain_repository(
                report_text
                + "\n\nDocumentation:\n"
                + documentation_text
            )
        )

        # Analyze Project Dependencies
        project_dependencies = (
            detect_project_dependencies(
                repo_path
            )
        )

        # Analyze Project Documentation
        documentation = (
            analyze_documentation(
                repo_path
            )
        )

        # Deployment Explanation
        deployment_explanation = (
            explain_deployment(
                report_text
            )
        )

        # Cleanup Repository
        cleanup_repository(repo_path)

        # Print Project Analysis    
        print("\nPROJECT ANALYSIS")
        print("=" * 60)

        # Print Technologies Detected
        print("\nTechnologies Detected:")

        if technologies:
            for tech in sorted(
                technologies
            ):
                print(f"- {tech}")
        else:
            print(
                "No technologies detected"
            )

        # Print Files Found
        print(
            f"\nTotal Files Found: {len(files)}"
        )

        # Print Required Tools
        print("\nRequired Tools:")

        if dependencies:
            for dep in dependencies:
                print(f"- {dep}")
        else:
            print(
                "No tools detected"
            )

        # Print Environment Validation
        print(
            "\nEnvironment Validation:"
        )

        if environment_status:

            for tool, status in (
                environment_status.items()
            ):

                symbol = (
                    "✓"
                    if status
                    else "✗"
                )

                print(
                    f"{tool:<15} {symbol}"
                )
        
        # Print Project Type
        print("\nProject Type:")
        print(project_type)

        # Print Project Structure
        print(
            "\nProject Structure:"
        )

        if project_structure:
            for directory in project_structure:
                print(
                    f"- {directory}"
                )

        if terraform_components:

            print(
                "\nInfrastructure Components:"
            )

            for component in (
                terraform_components
            ):
                print(
                    f"- {component}"
                )

        else:

            print(
                "\nDetected Services:"
            )

            if services:
                for service in services:
                    print(
                        f"- {service}"
                    )
            else:
                print(
                    "No services detected"
                )

        # Print Project Dependencies
        print(
            "\nProject Dependencies:"
        )

        if project_dependencies:

            for file, deps in (
                project_dependencies.items()
            ):

                print(f"\n{file}")

                if deps.get(
                    "dependencies"
                ):

                    print(
                        "Dependencies:"
                    )

                    for dep in deps[
                        "dependencies"
                    ]:
                        print(
                            f"  - {dep}"
                        )

                if deps.get(
                    "devDependencies"
                ):

                    print(
                        "Dev Dependencies:"
                    )

                    for dep in deps[
                        "devDependencies"
                    ]:
                        print(
                            f"  - {dep}"
                        )

        else:

            print(
                "No package dependencies found"
            )

        # Print Kubernetes Findings
        print(
            "\nKubernetes Findings:"
        )

        if k8s_findings:

            for finding in (
                k8s_findings
            ):
                print(
                    f"- {finding}"
                )

        else:
            print(
                "No issues detected"
            )

        # Print Docker Findings
        print(
            "\nDocker Findings:"
        )

        if docker_findings:

            for finding in (
                docker_findings
            ):
                print(
                    f"- {finding}"
                )

        else:
            print(
                "No issues detected"
            )

        # Print Terraform Findings
        print(
            "\nTerraform Findings:"
        )

        if terraform_findings:

            for finding in (
                terraform_findings
            ):
                print(
                    f"- {finding}"
                )

        else:
            print(
                "No issues detected"
            )

        # Print CI/CD Analysis
        print("\nCI/CD Analysis:")
        print("=" * 60)

        if pipeline_tools:

            print("\nPipeline Tools:")

            for tool in pipeline_tools:

                print(f"- {tool}")

            print("\nPipeline Files:")

            for file in workflow_files:

                print(f"- {file}")

        else:

            print(
                "No CI/CD pipeline detected"
            )

        # Print Architecture
        print("\nArchitecture Flow:")
        print("-" * 60)
        print(architecture)

        # Print AI Summary
        print("\nAI Repository Analysis:")
        print("=" * 60)
        print(ai_summary)

        # Print Deployment Explanation
        print("\nDeployment Explanation:")
        print("=" * 60)
        print(deployment_explanation)

        # Print Generated Report
        print(
            f"\nReport Generated: {report_file}"
        )

        # Print Setup Guide
        print("\nSetup Guide:")
        print("=" * 60)
        print(setup_guide)

        # Print Troubleshooting Guide
        print("\nTroubleshooting Guide:")
        print("=" * 60)
        print(troubleshooting_guide)

        # Print Interview Questions
        print("\nInterview Questions:")
        print("=" * 60)
        print(interview_questions)

    except Exception as e:

        print(
            f"\nError: {e}"
        )

    finally:

        if (
            is_git_repo
            and repo_path
        ):
            cleanup_repository(
                repo_path
            )


if __name__ == "__main__":
    main()