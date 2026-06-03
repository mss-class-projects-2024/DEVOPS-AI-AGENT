def classify_project(technologies):

    if "Terraform" in technologies:
        return "Infrastructure as Code Project"

    if "Kubernetes" in technologies:
        return "Cloud Native Microservices Application"

    if "Docker" in technologies:
        return "Containerized Application"

    return "Unknown Project"