def generate_interview_questions(
    technologies,
    services,
    terraform_components
):

    questions = []

    questions.append(
        "PROJECT INTERVIEW QUESTIONS"
    )

    questions.append("=" * 50)

    # Kubernetes

    if "Kubernetes" in technologies:

        questions.extend([

            "\nKubernetes Questions:",

            "1. What is the difference between a Deployment and a Pod?",

            "2. What is CrashLoopBackOff and how do you troubleshoot it?",

            "3. What are readinessProbe and livenessProbe?",

            "4. How do Services communicate inside Kubernetes?",

            "5. How would you debug a pod that cannot connect to a database?",

            "6. What is an HPA and how does it work?",

            "7. What is the difference between ClusterIP, NodePort and LoadBalancer?"
        ])

    # Docker

    if "Docker" in technologies:

        questions.extend([

            "\nDocker Questions:",

            "1. What is the difference between Docker Image and Container?",

            "2. What is the purpose of HEALTHCHECK in Docker?",

            "3. Why should containers avoid running as root?",

            "4. What is the difference between CMD and ENTRYPOINT?",

            "5. How do multi-stage builds improve Docker images?"
        ])

    # Terraform

    if "Terraform" in technologies:

        questions.extend([

            "\nTerraform Questions:",

            "1. What is Terraform state?",

            "2. What is the difference between terraform plan and terraform apply?",

            "3. How do Terraform modules work?",

            "4. Why should hardcoded values be avoided in Terraform?",

            "5. What is remote state and why is it important?",

            "6. How would you manage Terraform state in a team environment?"
        ])

    # AWS Infrastructure

    if terraform_components:

        questions.extend([

            "\nAWS Infrastructure Questions:",

            "1. Explain the architecture of this project.",

            "2. Why is a VPC required?",

            "3. What is the purpose of Security Groups?",

            "4. How does an Application Load Balancer work?",

            "5. Why is Amazon RDS used instead of self-managed MySQL?",

            "6. What is the role of CloudFront CDN?",

            "7. What is the purpose of a Bastion Host?"
        ])

    # Node.js

    if "Node.js" in technologies:

        questions.extend([

            "\nNode.js Questions:",

            "1. What is Express.js?",

            "2. How do Node.js microservices communicate?",

            "3. What is Prisma ORM?",

            "4. How do you manage environment variables in Node.js?",

            "5. What is the event loop?"
        ])

    # Service-specific questions

    if services:

        questions.append(
            "\nProject Specific Questions:"
        )

        for service in services:

            questions.append(
                f"- Explain the purpose of {service} service."
            )

            questions.append(
                f"- How would you troubleshoot failures in {service}?"
            )

    return "\n".join(
        questions
    )