from ai.deployment_explainer import (
    explain_deployment
)

with open(
    "reports/project_report.md",
    "r",
    encoding="utf-8"
) as f:

    report_text = f.read()

deployment_flow = (
    explain_deployment(
        report_text
    )
)

print(deployment_flow)