def generate_architecture(
    project_type,
    services=None,
    terraform_components=None
):

    services = services or []
    terraform_components = (
        terraform_components or []
    )

    architecture = []

    # Terraform Infrastructure

    if terraform_components:

        architecture.append(
            "Internet"
        )

        if (
            "CloudFront CDN"
            in terraform_components
        ):
            architecture.append(
                "   ↓"
            )
            architecture.append(
                "CloudFront"
            )

        if (
            "Load Balancer"
            in terraform_components
        ):
            architecture.append(
                "   ↓"
            )
            architecture.append(
                "Application Load Balancer"
            )

        if (
            "Frontend"
            in terraform_components
        ):
            architecture.append(
                "   ↓"
            )
            architecture.append(
                "Frontend"
            )

        if (
            "Backend"
            in terraform_components
        ):
            architecture.append(
                "   ↓"
            )
            architecture.append(
                "Backend"
            )

        if (
            "RDS"
            in terraform_components
        ):
            architecture.append(
                "   ↓"
            )
            architecture.append(
                "Amazon RDS"
            )

    # Kubernetes / Microservices

    elif services:

        architecture.extend([
            "Developer",
            "   ↓",
            "GitHub",
            "   ↓",
            "Docker",
            "   ↓",
            "Kubernetes"
        ])

        for service in services:

            architecture.append(
                "   ↓"
            )

            architecture.append(
                service
            )

    else:

        architecture.append(
            "Architecture could not be generated"
        )

    return "\n".join(
        architecture
    )