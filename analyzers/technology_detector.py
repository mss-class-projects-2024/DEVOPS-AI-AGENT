def detect_technologies(files):
    technologies = set()

    for file in files:

        if "Dockerfile" in file:
            technologies.add("Docker")

        if file.endswith(".tf"):
            technologies.add("Terraform")

        if "Jenkinsfile" in file:
            technologies.add("Jenkins")

        if "docker-compose" in file:
            technologies.add("Docker Compose")

        if "package.json" in file:
            technologies.add("Node.js")

        if "requirements.txt" in file:
            technologies.add("Python")

        if "deployment.yaml" in file or "service.yaml" in file:
            technologies.add("Kubernetes")

    return technologies