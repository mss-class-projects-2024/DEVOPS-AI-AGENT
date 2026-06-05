def generate_interview_questions(
    technologies,
    services,
    terraform_components
):

    questions = []

    questions.append(
        "PROJECT INTERVIEW QUESTIONS"
    )

    questions.append(
        "=" * 50
    )

    # Kubernetes
    if any(
        "kubernetes" in str(tech).lower()
        for tech in technologies
    ):

        questions.extend([
            "",
            "Kubernetes Questions:",
            "1. What is the difference between a Deployment and a Pod?",
            "2. What is CrashLoopBackOff and how do you troubleshoot it?",
            "3. What are readinessProbe and livenessProbe?",
            "4. How do Services communicate inside Kubernetes?",
            "5. How would you debug a pod that cannot connect to a database?",
            "6. What is an HPA and how does it work?",
            "7. What is the difference between ClusterIP, NodePort and LoadBalancer?"
        ])

    # Docker
    if any(
        "docker" in str(tech).lower()
        for tech in technologies
    ):

        questions.extend([
            "",
            "Docker Questions:",
            "1. What is the difference between Docker Image and Container?",
            "2. What is the purpose of HEALTHCHECK in Docker?",
            "3. Why should containers avoid running as root?",
            "4. What is the difference between CMD and ENTRYPOINT?",
            "5. How do multi-stage builds improve Docker images?"
        ])

    # Node.js
    if any(
        tech.lower() in [
            "node.js",
            "nodejs",
            "express"
        ]
        for tech in technologies
    ):

        questions.extend([
            "",
            "Node.js Questions:",
            "1. What is Express.js?",
            "2. How do Node.js microservices communicate?",
            "3. What is Prisma ORM?",
            "4. How do you manage environment variables in Node.js?",
            "5. What is the event loop?"
        ])

    # Project Services
    questions.extend([
        "",
        "Project Specific Questions:"
    ])

    service_questions = []

    for service in services:

        service_name = service.lower()

        # Ignore common packages
        if service_name in {
            "react",
            "axios",
            "vite",
            "typescript",
            "express",
            "prisma"
        }:
            continue

        service_questions.extend([
            f"- Explain the purpose of {service}.",
            f"- How would you troubleshoot failures in {service}?",
            f"- How does {service} communicate with other services?"
        ])

    questions.extend(service_questions)

    # Terraform
    if terraform_components:

        questions.extend([
            "",
            "Terraform Questions:",
            "1. What is Terraform state?",
            "2. Why should Terraform state be stored remotely?",
            "3. What is the purpose of terraform plan?",
            "4. Explain Terraform modules.",
            "5. How do you manage secrets in Terraform?"
        ])

    return "\n".join(questions)