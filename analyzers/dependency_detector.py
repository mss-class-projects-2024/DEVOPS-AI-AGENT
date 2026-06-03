def detect_dependencies(technologies):

    dependencies = set()

    if "Docker" in technologies:
        dependencies.add("Docker")

    if "Kubernetes" in technologies:
        dependencies.add("kubectl")
        dependencies.add("eksctl")

    if "Terraform" in technologies:
        dependencies.add("Terraform")

    if "Node.js" in technologies:
        dependencies.add("Node.js")

    dependencies.add("Git")

    return sorted(dependencies)