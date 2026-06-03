def generate_troubleshooting_guide(
    k8s_findings,
    docker_findings,
    terraform_findings
):

    guide = []

    guide.append(
        "TROUBLESHOOTING GUIDE"
    )

    guide.append("=" * 50)

    # Kubernetes Findings

    if k8s_findings:

        guide.append(
            "\nKubernetes Issues:"
        )

        for finding in k8s_findings:

            guide.append(
                f"\nIssue: {finding}"
            )

            if "readinessProbe" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Add readinessProbe to Deployment."
                )

                guide.append(
                    "- Verify application health endpoint."
                )

            elif "livenessProbe" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Add livenessProbe."
                )

                guide.append(
                    "- Prevent unhealthy pods from staying alive."
                )

            elif "latest image tag" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Replace latest with a versioned tag."
                )

                guide.append(
                    "- Example: app:v1.0.0"
                )

    # Docker Findings

    if docker_findings:

        guide.append(
            "\nDocker Issues:"
        )

        for finding in docker_findings:

            guide.append(
                f"\nIssue: {finding}"
            )

            if "HEALTHCHECK" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Add HEALTHCHECK instruction."
                )

                guide.append(
                    "- Ensure container health can be verified."
                )

            elif "root user" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Create a non-root user."
                )

                guide.append(
                    "- Use USER directive."
                )

            elif "latest base image" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Pin the image version."
                )

                guide.append(
                    "- Example: node:20-alpine"
                )

    # Terraform Findings

    if terraform_findings:

        guide.append(
            "\nTerraform Issues:"
        )

        for finding in terraform_findings:

            guide.append(
                f"\nIssue: {finding}"
            )

            if "Hardcoded AWS region" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Use Terraform variables."
                )

                guide.append(
                    '- Example: var.aws_region'
                )

            elif "instance type" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Parameterize instance_type."
                )

                guide.append(
                    "- Use terraform.tfvars."
                )

            elif "AMI" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Avoid hardcoded AMIs."
                )

                guide.append(
                    "- Use AWS SSM Parameter Store."
                )

            elif "provider.tf" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Create provider.tf."
                )

                guide.append(
                    "- Configure AWS provider."
                )

            elif "versions.tf" in finding:

                guide.append(
                    "Resolution:"
                )

                guide.append(
                    "- Create versions.tf."
                )

                guide.append(
                    "- Define Terraform version constraints."
                )

    if (
        not k8s_findings
        and not docker_findings
        and not terraform_findings
    ):

        guide.append(
            "\nNo issues detected."
        )

    return "\n".join(
        guide
    )