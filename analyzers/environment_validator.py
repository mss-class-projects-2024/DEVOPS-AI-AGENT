import shutil


def check_tool(tool_name):
    return shutil.which(
        tool_name
    ) is not None


def validate_environment(
    dependencies
):

    results = {}

    tool_mapping = {
        "Docker": "docker",
        "Git": "git",
        "kubectl": "kubectl",
        "eksctl": "eksctl",
        "Terraform": "terraform",
        "Node.js": "node"
    }

    for dep in dependencies:

        command = tool_mapping.get(
            dep
        )

        if command:

            results[dep] = (
                check_tool(command)
            )

        else:

            results[dep] = False

    return results