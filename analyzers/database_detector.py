import os
import re


def detect_databases(repo_path):
    """
    Detect databases used in a repository.

    Returns:
    {
        "databases": [...],
        "findings": [...]
    }
    """

    databases = set()
    findings = []

    db_patterns = {
        "MySQL": [
            r"mysql",
            r"MYSQL_",
            r"mysql:"
        ],
        "PostgreSQL": [
            r"postgres",
            r"POSTGRES_",
            r"postgres:"
        ],
        "MongoDB": [
            r"mongodb",
            r"mongo:"
        ],
        "Redis": [
            r"redis",
            r"redis:"
        ],
        "MariaDB": [
            r"mariadb",
            r"mariadb:"
        ],
        "SQLite": [
            r"sqlite"
        ],
        "Oracle": [
            r"oracle"
        ],
        "SQL Server": [
            r"sqlserver",
            r"mssql"
        ],
        "DynamoDB": [
            r"dynamodb"
        ],
        "RDS": [
            r"rds.amazonaws.com"
        ]
    }

    prisma_db_map = {
        "mysql": "MySQL",
        "postgresql": "PostgreSQL",
        "sqlite": "SQLite",
        "sqlserver": "SQL Server",
        "mongodb": "MongoDB"
    }

    for root, _, files in os.walk(repo_path):

        for file in files:

            file_path = os.path.join(root, file)

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                content_lower = content.lower()

                # General database detection
                for db_name, patterns in db_patterns.items():

                    for pattern in patterns:

                        if re.search(
                            pattern,
                            content_lower
                        ):
                            databases.add(db_name)

                # Prisma schema detection
                if file == "schema.prisma":

                    provider_match = re.search(
                        r'provider\s*=\s*"([^"]+)"',
                        content_lower
                    )

                    if provider_match:

                        provider = (
                            provider_match.group(1)
                            .strip()
                            .lower()
                        )

                        db = prisma_db_map.get(provider)

                        if db:
                            databases.add(db)

                # Docker Compose database services
                if (
                    file.endswith(".yml")
                    or file.endswith(".yaml")
                ):

                    if "mysql:" in content_lower:
                        findings.append(
                            f"{file}: MySQL service detected"
                        )

                    if "postgres:" in content_lower:
                        findings.append(
                            f"{file}: PostgreSQL service detected"
                        )

                    if "mongo:" in content_lower:
                        findings.append(
                            f"{file}: MongoDB service detected"
                        )

                    if "redis:" in content_lower:
                        findings.append(
                            f"{file}: Redis service detected"
                        )

            except Exception:
                continue

    return {
        "databases": sorted(databases),
        "findings": findings
    }