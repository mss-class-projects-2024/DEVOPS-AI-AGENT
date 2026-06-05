# analyzers/jenkins_analyzer.py

from pathlib import Path
import re


def analyze_jenkins(repo_path):

    findings = []
    stages = []
    tools = []

    jenkinsfile = None

    for file in Path(repo_path).rglob("Jenkinsfile"):

        jenkinsfile = file
        break

    if not jenkinsfile:

        findings.append(
            "No Jenkinsfile found"
        )

        return {
            "findings": findings,
            "stages": stages,
            "tools": tools
        }

    findings.append(
        f"Jenkinsfile detected: {jenkinsfile}"
    )

    try:

        content = jenkinsfile.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception as e:

        findings.append(
            f"Unable to read Jenkinsfile: {e}"
        )

        return {
            "findings": findings,
            "stages": stages,
            "tools": tools
        }

    # --------------------------------------------------
    # Pipeline Type
    # --------------------------------------------------

    if "pipeline {" in content:

        findings.append(
            "Declarative Jenkins Pipeline detected"
        )

    if "node {" in content:

        findings.append(
            "Scripted Jenkins Pipeline detected"
        )

    # --------------------------------------------------
    # Stages
    # --------------------------------------------------

    stage_matches = re.findall(
        r"stage\s*\(\s*['\"]([^'\"]+)['\"]\s*\)",
        content
    )

    stages.extend(stage_matches)

    # --------------------------------------------------
    # Docker
    # --------------------------------------------------

    if (
        "docker build" in content
        or "docker.build" in content
    ):

        tools.append("Docker")

        findings.append(
            "Docker build stage detected"
        )

    # --------------------------------------------------
    # Kubernetes
    # --------------------------------------------------

    if "kubectl" in content:

        tools.append("Kubernetes")

        findings.append(
            "Kubernetes deployment detected"
        )

    # --------------------------------------------------
    # Terraform
    # --------------------------------------------------

    terraform_keywords = [
        "terraform init",
        "terraform plan",
        "terraform apply"
    ]

    for keyword in terraform_keywords:

        if keyword in content:

            tools.append("Terraform")

            findings.append(
                f"Terraform command detected: {keyword}"
            )

    # --------------------------------------------------
    # SonarQube
    # --------------------------------------------------

    sonar_keywords = [
        "sonarqube",
        "sonar-scanner",
        "withSonarQubeEnv"
    ]

    if any(
        keyword.lower() in content.lower()
        for keyword in sonar_keywords
    ):

        tools.append("SonarQube")

        findings.append(
            "SonarQube integration detected"
        )

    # --------------------------------------------------
    # Security Scanning
    # --------------------------------------------------

    security_tools = [
        "trivy",
        "snyk",
        "owasp"
    ]

    for tool in security_tools:

        if tool.lower() in content.lower():

            findings.append(
                f"Security scan detected: {tool}"
            )

            tools.append(tool)

    # --------------------------------------------------
    # Best Practice Checks
    # --------------------------------------------------

    if not stage_matches:

        findings.append(
            "No pipeline stages detected"
        )

    if "post {" not in content:

        findings.append(
            "Missing post-build actions"
        )

    if "agent any" not in content:

        findings.append(
            "Pipeline does not use agent any"
        )

    return {
        "findings": sorted(
            list(set(findings))
        ),
        "stages": sorted(
            list(set(stages))
        ),
        "tools": sorted(
            list(set(tools))
        )
    }