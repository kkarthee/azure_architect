# DevOps Architecture - Onboarding & How to adapt

Contents
- diagrams/devops-architecture.svg
- ppt/devops-architecture-slides.md
- pipelines/azure-pipelines.yml
- iac/terraform/main.tf
- iac/terraform/variables.tf
- iac/ansible/deploy.yml
- iac/ansible/hosts

How to use these artifacts
1. Diagram
   - Open diagrams/devops-architecture.svg in Inkscape or Illustrator to modify visuals or add official Azure icons.
   - Export PNG: inkscape diagrams/devops-architecture.svg --export-type=png --export-filename=diagrams/devops-architecture.png

2. Slide deck
   - Convert markdown to PPTX:
     - Ensure pandoc is installed.
     - pandoc ppt/devops-architecture-slides.md -t pptx -o ppt/devops-architecture.pptx
   - Or create a blank PPTX and paste each slide content, and insert the SVG on the architecture slide.

3. Azure Pipelines
   - pipelines/azure-pipelines.yml is a starter CI/CD pipeline.
   - Replace placeholders (registry, service connections, secrets).
   - Create service connections in Azure DevOps:
     - Azure Resource Manager service connection (Terraform)
     - Docker registry connection (ACR)
     - SonarQube endpoint

4. Terraform
   - iac/terraform/main.tf includes minimal resources (resource group, ACR, Log Analytics).
   - Configure remote state using Azure Storage with lock (recommended).
   - Use workspaces for environments: dev/test/stage/preprod/prod

5. Ansible
   - iac/ansible/deploy.yml is a simple playbook skeleton.
   - Use inventories per environment in iac/ansible/hosts
   - Retrieve secrets from Key Vault (via pipeline) and pass to Ansible via --extra-vars or env vars.

6. Secrets & Identity
   - Use Managed Identities where possible.
   - Limit Key Vault access to pipeline service principal or managed identity and runtime identities.
   - Rotate service principals and certificates on a schedule.

7. Monitoring & Security
   - Configure AKS / App Service to send logs to Log Analytics.
   - Instrument apps with Application Insights SDK.
   - Configure Defender for Cloud and integrate with Azure Sentinel.
   - Create Sentinel connectors and tune threat detection rules; create playbooks for ServiceNow integration.

8. ServiceNow
   - Use Sentinel playbooks or Logic Apps to create incidents in ServiceNow.
   - Ensure secure credentials stored in Key Vault and accessed by playbooks as needed.

9. Next steps & checklist
   - Confirm network connectivity (VPN/ExpressRoute) between on‑prem and Azure Log Analytics.
   - Create pipeline service connections and ensure least privilege.
   - Run pilot with dev environment, validate telemetry and security connectors.
   - Tune Sentinel rules and build dashboards/workbooks.

Contact
- Author: kkarthee
- Date: 2026-02-01
