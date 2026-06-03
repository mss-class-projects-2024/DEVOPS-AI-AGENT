def generate_setup_guide(
    technologies,
    dependencies,
    services,
    terraform_components
):

    guide = []

    guide.append(
        "PROJECT SETUP GUIDE"
    )

    guide.append("=" * 50)

    guide.append("\nPrerequisites:")

    for dependency in dependencies:

        guide.append(
            f"- Install {dependency}"
        )

    # Kubernetes Project

    if (
        "Kubernetes" in technologies
    ):

        guide.extend([
            "",
            "Kubernetes Setup:",
            "1. Install kubectl",
            "2. Install eksctl",
            "3. Configure AWS CLI",
            "4. Create EKS Cluster",
            "5. Build Docker Images",
            "6. Push Images to ECR",
            "7. Apply Kubernetes Manifests",
            "",
            "Commands:",
            "kubectl apply -f k8s/"
        ])

    # Docker Project

    if (
        "Docker" in technologies
    ):

        guide.extend([
            "",
            "Docker Setup:",
            "1. Install Docker Desktop",
            "2. Build Docker Images",
            "3. Run Containers",
            "",
            "Commands:",
            "docker build -t app .",
            "docker compose up -d"
        ])

    # Terraform Project

    if terraform_components:

        guide.extend([
            "",
            "Terraform Setup:",
            "1. Install Terraform",
            "2. Configure AWS Credentials",
            "3. Initialize Terraform",
            "4. Validate Configuration",
            "5. Plan Infrastructure",
            "6. Apply Infrastructure",
            "",
            "Commands:",
            "terraform init",
            "terraform validate",
            "terraform plan",
            "terraform apply"
        ])

    return "\n".join(
        guide
    )