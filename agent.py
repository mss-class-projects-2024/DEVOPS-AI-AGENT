from analyzers.git_analyzer import scan_repository

from analyzers.github_analyzer import (
    clone_repository,
    cleanup_repository
)

from analyzers.technology_detector import (
    detect_technologies
)

from analyzers.project_classifier import (
    classify_project
)

from analyzers.dependency_detector import (
    detect_dependencies
)

from analyzers.environment_validator import (
    validate_environment
)

from analyzers.project_structure import (
    analyze_structure
)

from analyzers.service_detector import (
    detect_services
)

from analyzers.k8s_analyzer import (
    analyze_k8s
)
def main():

    repo_input = input(
        "Enter local path or Git URL: "
    ).strip()

    is_git_repo = (
        repo_input.startswith("http://")
        or
        repo_input.startswith("https://")
    )

    try:

        if is_git_repo:

            repo_path = clone_repository(
                repo_input
            )

        else:

            repo_path = repo_input

        files = scan_repository(
            repo_path
        )
        project_structure = (
            analyze_structure(repo_path)
        )

        services = detect_services(
            repo_path
        )
        k8s_findings = analyze_k8s(repo_path)

        technologies = detect_technologies(
            files
        )

        dependencies = detect_dependencies(
            technologies
        )

        environment_status = (
            validate_environment(
                dependencies
            )
        )

        project_type = classify_project(
            technologies
        )

        print("\nPROJECT ANALYSIS")
        print("=" * 60)

        print("\nTechnologies Detected:")

        if technologies:

            for tech in sorted(technologies):
                print(f"- {tech}")

        else:

            print(
                "No technologies detected"
            )

        print(
            f"\nTotal Files Found: {len(files)}"
        )

        print("\nRequired Tools:")

        for dep in dependencies:
            print(f"- {dep}")

        print("\nEnvironment Validation:")

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

        print("\nProject Type:")
        print(project_type)

        print("\nProject Structure:")
        for directory in project_structure:
            print(f"- {directory}")

        print("\nDetected Services:")
        for service in services:
            print(f"- {service}")

        print("\nKubernetes Findings:")
        if k8s_findings:
            for finding in k8s_findings:
                print(f"- {finding}")
        else:
            print("No issues detected")  

    except Exception as e:

        print(
            f"\nError: {e}"
        )

    finally:

        if (
            is_git_repo
            and 'repo_path' in locals()
        ):

            cleanup_repository(
                repo_path
            )


if __name__ == "__main__":
    main()