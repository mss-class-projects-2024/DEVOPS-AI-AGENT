# analyzers/recommendation_engine.py

def generate_recommendations(
    technologies=None,
    dependencies=None,
    documentation=None,
    k8s_findings=None,
    docker_findings=None,
    terraform_findings=None,
    pipeline_tools=None,
    workflow_files=None,
):
    """
    Generate project improvement recommendations
    based on analysis findings.
    """

    recommendations = []

    technologies = technologies or []
    dependencies = dependencies or []
    documentation = documentation or []
    k8s_findings = k8s_findings or []
    docker_findings = docker_findings or []
    terraform_findings = terraform_findings or []
    pipeline_tools = pipeline_tools or []
    workflow_files = workflow_files or []

    # -------------------------------------------------
    # Documentation Recommendations
    # -------------------------------------------------
    if not documentation:

        recommendations.append(
            "Add project documentation (README.md) explaining setup, usage, and deployment."
        )

    docs_lower = []

    for doc in documentation:

        if isinstance(doc, dict):

            docs_lower.append(
                doc.get(
                    "file",
                    ""
                ).lower()
            )

    if not any(
        "readme" in doc
        for doc in docs_lower
    ):
        recommendations.append(
            "Create a README.md file with installation and usage instructions."
        )

    if not any(
        "contributing" in doc
        for doc in docs_lower
    ):
        recommendations.append(
            "Consider adding CONTRIBUTING.md for collaboration guidelines."
        )

    # -------------------------------------------------
    # Dependency Recommendations
    # -------------------------------------------------

    if dependencies:
        recommendations.append(
            "Review dependencies regularly and remove unused packages."
        )

    # -------------------------------------------------
    # Docker Recommendations
    # -------------------------------------------------

    if not docker_findings:
        recommendations.append(
            "Consider containerizing the application using Docker."
        )
    else:
        recommendations.append(
            "Validate Docker images for security vulnerabilities using Trivy or Docker Scout."
        )

    # -------------------------------------------------
    # Kubernetes Recommendations
    # -------------------------------------------------

    if k8s_findings:
        recommendations.append(
            "Implement resource requests and limits for Kubernetes workloads."
        )
        recommendations.append(
            "Add liveness and readiness probes to improve application reliability."
        )
    else:
        recommendations.append(
            "Consider Kubernetes manifests or Helm charts for scalable deployments."
        )

    # -------------------------------------------------
    # Terraform Recommendations
    # -------------------------------------------------

    if terraform_findings:
        recommendations.append(
            "Store Terraform state remotely (S3 + DynamoDB locking recommended)."
        )
        recommendations.append(
            "Run terraform fmt and terraform validate in CI/CD pipelines."
        )
    else:
        recommendations.append(
            "Use Infrastructure as Code (Terraform) to provision cloud resources."
        )

    # -------------------------------------------------
    # CI/CD Recommendations
    # -------------------------------------------------

    if pipeline_tools or workflow_files:
        recommendations.append(
            "Integrate automated security scanning into CI/CD pipelines."
        )
        recommendations.append(
            "Add automated testing before deployment stages."
        )
    else:
        recommendations.append(
            "Implement CI/CD using GitHub Actions, Jenkins, GitLab CI, or Azure DevOps."
        )

    # -------------------------------------------------
    # Technology-Specific Recommendations
    # -------------------------------------------------

    tech_lower = [tech.lower() for tech in technologies]

    if any("python" in tech for tech in tech_lower):
        recommendations.append(
            "Use virtual environments and dependency pinning (requirements.txt or pyproject.toml)."
        )

    if any("node" in tech for tech in tech_lower):
        recommendations.append(
            "Enable npm audit or Dependabot for dependency management."
        )

    if any("java" in tech for tech in tech_lower):
        recommendations.append(
            "Use Maven/Gradle dependency scanning and code quality tools such as SonarQube."
        )

    # -------------------------------------------------
    # Security Recommendations
    # -------------------------------------------------

    recommendations.append(
        "Enable secret scanning to prevent credentials from being committed to source control."
    )

    recommendations.append(
        "Use least-privilege IAM roles and service accounts."
    )

    recommendations.append(
        "Perform regular vulnerability and compliance scans."
    )

    return sorted(set(recommendations))