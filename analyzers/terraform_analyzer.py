from pathlib import Path


def analyze_terraform(repo_path):

    findings = []
    components = []

    tf_files = list(
        Path(repo_path).rglob("*.tf")
    )

    if not tf_files:
        return [], []

    component_keywords = {
        "vpc": "VPC",
        "sg": "Security Groups",
        "security": "Security Groups",
        "rds": "RDS",
        "alb": "Load Balancer",
        "frontend": "Frontend",
        "backend": "Backend",
        "vpn": "VPN",
        "bastion": "Bastion Host",
        "cdn": "CloudFront CDN",
        "acm": "AWS Certificate Manager"
    }

    for tf_file in tf_files:

        relative_path = str(
            tf_file.relative_to(repo_path)
        )

        relative_path_lower = (
            relative_path.lower()
        )

        try:

            content = tf_file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

        except Exception:
            continue

        # Detect Infrastructure Components

        for keyword, component in (
            component_keywords.items()
        ):

            if keyword in relative_path_lower:

                if component not in components:

                    components.append(
                        component
                    )

        # Terraform Checks

        if 'instance_type = "' in content:

            findings.append(
                f"{relative_path}: Hardcoded instance type"
            )

        if 'ami = "' in content:

            findings.append(
                f"{relative_path}: Hardcoded AMI"
            )

        if (
            'region = "' in content
            and "provider" in tf_file.name.lower()
        ):

            findings.append(
                f"{relative_path}: Hardcoded AWS region (warning)"
            )

    # Check Required Terraform Files

    file_names = [
        file.name.lower()
        for file in tf_files
    ]

    if "provider.tf" not in file_names:

        findings.append(
            "Missing provider.tf"
        )

    if "versions.tf" not in file_names:

        findings.append(
            "Missing versions.tf"
        )

    # Remove Duplicates

    findings = sorted(
        list(set(findings))
    )

    components = sorted(
        list(set(components))
    )

    return findings, components