from analyzers.git_analyzer import scan_repository
from analyzers.github_analyzer import clone_repository, cleanup_repository
from analyzers.technology_detector import detect_technologies
from analyzers.project_classifier import classify_project
from analyzers.dependency_detector import detect_dependencies
from analyzers.environment_validator import validate_environment
from analyzers.project_structure import analyze_structure
from analyzers.service_detector import detect_services
from analyzers.database_detector import detect_databases
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
from analyzers.recommendation_engine import generate_recommendations
from ai.repository_explainer import explain_repository
from ai.deployment_explainer import explain_deployment
from analyzers.documentation_analyzer import analyze_documentation


import os
import traceback
from pathlib import Path

def main():
    # Get repository input from user
    repo_input = input(
        "Enter local path or Git URL: "
    ).strip()

    is_git_repo = (
        repo_input.startswith("http://")
        or repo_input.startswith("https://")
    )

    repo_path = None

    try:
        # git clone if URL, otherwise use local path
        if is_git_repo:

            repo_path = clone_repository(
                repo_input
            )

        else:

            if not os.path.exists(
                repo_input
            ):

                raise Exception(
                    f"Path does not exist: {repo_input}"
                )

            repo_path = repo_input

        files = scan_repository(repo_path)

        technologies = (
            detect_technologies(files)
            or set()
        )

        dependencies = (
            detect_dependencies(
                technologies
            )
            or []
        )

        environment_status = (
            validate_environment(
                dependencies
            )
        )

        project_type = classify_project(technologies)

        project_structure = (
            analyze_structure(
                repo_path
            )
        )

        # Services Detection
        services = (
            detect_services(
                repo_path
            )
            or []
        )

        # Database Detection
        database_result = detect_databases(
            repo_path
        )

        databases = database_result.get(
            "databases",
            []
        )

        database_findings = database_result.get(
            "findings",
            []
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
            or []
        )

        # Kubernetes Analysis
        k8s_findings = (
            analyze_k8s(
                repo_path
            )
            or []
        )

        # Docker Analysis
        docker_findings = (
            analyze_docker(
                repo_path
            )
            or []
        )

        # Terraform Analysis
        terraform_result = analyze_terraform(
            repo_path
        )

        if terraform_result:
            terraform_findings, terraform_components = terraform_result
        else:
            terraform_findings = []
            terraform_components = []

        # CI/CD Analysis
        cicd_result = analyze_cicd(
            repo_path
        )

        if cicd_result:
            pipeline_tools, workflow_files = cicd_result
        else:
            pipeline_tools = []
            workflow_files = []

        # Recommendation Generation
        recommendations = generate_recommendations(
            technologies=technologies,
            dependencies=dependencies,
            documentation=documentation,
            k8s_findings=k8s_findings,
            docker_findings=docker_findings,
            terraform_findings=terraform_findings,
            pipeline_tools=pipeline_tools,
            workflow_files=workflow_files,
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
        )

        # Repository Explanation
        if not report_file:
            raise Exception(
                "Report generator returned no file path"
            )

        if not os.path.exists(report_file):
            raise Exception(
                f"Report file not found: {report_file}"
            )

        with open(
            report_file,
            "r",
            encoding="utf-8"
        ) as f:

            report_text = f.read()

        documentation_text = ""

        # Combine documentation content for LLM analysis
        MAX_DOC_CHARS = 3000

        documentation_text = ""

        for doc in documentation:

            file_name = doc.get(
                "file",
                "Unknown File"
            )

            content = doc.get(
                "content"
            ) or ""

            documentation_text += (
                f"\n\nFILE: {file_name}\n"
            )

            documentation_text += (
                content[:MAX_DOC_CHARS]
            )

        MAX_AI_INPUT = 15000

        combined_input = (
            report_text
            + "\n\nDocumentation:\n"
            + documentation_text
        )

        combined_input = (
            combined_input[:MAX_AI_INPUT]
        )

        # Explain Repository using LLM
        ai_summary = (
            explain_repository(
                combined_input
            )
        )

        # Deployment Explainer
        deployment_explanation = (
            explain_deployment(
                combined_input
            )
        )

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

        # Print Detected Services
        if project_structure:
            for directory in project_structure:
                print(
                    f"- {directory}"
                )

        print("\nDetected Services:")

        # Print Detected Services
        if services:

            for service in services:

                print(
                    f"- {service}"
                )

        else:

            print(
                "No services detected"
            )

        # Database Detection Results
        print("\nDatabases Detected:")
        print("=" * 60)

        if databases:

            for db in databases:

                print(
                    f"- {db}"
                )

        else:

            print(
                "No databases detected"
            )
        # Database Findings Results
        print("\nDatabase Findings:")

        if database_findings:

            for finding in database_findings:

                print(
                    f"- {finding}"
                )

        else:

            print(
                "No database findings"
            )

        print("\nInfrastructure Components:")

        # Print Terraform Components
        if terraform_components:

            for component in terraform_components:

                print(
                    f"- {component}"
                )

        else:

            print(
                "No infrastructure detected"
            )
            
        # Create dependency report file

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        dependency_report = (
            reports_dir / "dependencies_report.txt"
        )

        with open(
            dependency_report,
            "w",
            encoding="utf-8"
        ) as dep_file:

            dep_file.write(
                "PROJECT DEPENDENCIES REPORT\n"
            )

            dep_file.write(
                "=" * 50 + "\n\n"
            )

            if project_dependencies:

                for file, deps in (
                    project_dependencies.items()
                ):

                    dep_file.write(
                        f"\n{file}\n"
                    )

                    dep_file.write(
                        "-" * 40 + "\n"
                    )

                    if deps.get("dependencies"):

                        dep_file.write(
                            "\nDependencies:\n"
                        )

                        for dep in deps["dependencies"]:

                            dep_file.write(
                                f"- {dep}\n"
                            )

                    if deps.get("devDependencies"):

                        dep_file.write(
                            "\nDev Dependencies:\n"
                        )

                        for dep in deps["devDependencies"]:

                            dep_file.write(
                                f"- {dep}\n"
                            )

        print("\nProject Dependencies:")
        print("=" * 60)

        if project_dependencies:

            for file, deps in project_dependencies.items():

                print(f"\n{file}")

                print(
                    f"Dependencies: {len(deps.get('dependencies', []))}"
                )

                print(
                    f"Dev Dependencies: {len(deps.get('devDependencies', []))}"
                )

        else:

            print(
                "No package dependencies found"
            )

        print(
            f"\nFull dependency report saved: "
            f"{dependency_report}"
        )
        # Print Documentation Files
        print("\nDocumentation Files:")
        print("=" * 60)

        if documentation:

            for doc in documentation:

                file_name = doc.get(
                    "file",
                    "Unknown File"
                )

                content = doc.get(
                    "content"
                ) or ""

                print(f"\n{file_name}")
                print(content[:300])

        else:

            print(
                "No documentation content found"
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

        # Print Recommendations
        print("\nRecommendations:")
        print("=" * 60)

        for rec in recommendations:
            print(f"- {rec}")

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

        traceback.print_exc()
        
    finally:

        if (
            is_git_repo
            and repo_path
            and os.path.exists(repo_path)
        ):
            cleanup_repository(
                repo_path
            )


if __name__ == "__main__":
    main()