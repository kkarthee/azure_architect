# DevOps Onboarding Guide

Welcome to the Azure DevOps Architecture project! This guide will help you get started with our DevOps practices and tooling.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [CI/CD Pipeline](#cicd-pipeline)
- [Infrastructure as Code](#infrastructure-as-code)
- [Configuration Management](#configuration-management)
- [Security Practices](#security-practices)
- [Troubleshooting](#troubleshooting)

## Overview

This repository contains the DevOps architecture and automation tooling for Azure-based applications. It includes:

- **Architecture Diagrams**: Visual representation of the DevOps workflow
- **CI/CD Pipelines**: Automated build and deployment pipelines
- **Infrastructure as Code (IaC)**: Terraform configurations for Azure resources
- **Configuration Management**: Ansible playbooks for application deployment
- **Documentation**: Comprehensive guides and best practices

## Prerequisites

Before you begin, ensure you have the following:

### Required Tools
- **Git**: Version control system
- **Azure CLI**: Command-line tools for Azure
- **Terraform**: Infrastructure as Code tool (v1.0+)
- **Ansible**: Configuration management tool (v2.9+)
- **Azure DevOps Account**: Access to organization and project

### Required Access
- Azure subscription with appropriate permissions
- Azure DevOps project access
- Git repository access (read/write)
- Service principal for automated deployments

### Installation

#### Azure CLI
```bash
# macOS
brew install azure-cli

# Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Windows
# Download from: https://aka.ms/installazurecliwindows
```

#### Terraform
```bash
# macOS
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

# Linux
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/

# Windows
# Download from: https://www.terraform.io/downloads
```

#### Ansible
```bash
# macOS/Linux
pip install ansible

# Or using package manager
sudo apt-get install ansible  # Ubuntu/Debian
sudo yum install ansible      # CentOS/RHEL
```

## Repository Structure

```
azure_architect/
├── diagrams/
│   ├── devops-architecture.svg     # Architecture diagram (SVG)
│   └── devops-architecture.png     # Architecture diagram (PNG)
├── ppt/
│   ├── devops-architecture.pptx         # PowerPoint presentation
│   └── devops-architecture-slides.md    # Markdown source for slides
├── pipelines/
│   └── azure-pipelines.yml         # Azure Pipelines configuration
├── iac/
│   ├── terraform/
│   │   ├── main.tf                 # Terraform main configuration
│   │   └── variables.tf            # Terraform variables
│   └── ansible/
│       ├── deploy.yml              # Ansible deployment playbook
│       └── hosts                   # Ansible inventory
├── README.md                       # Main project README
└── README-devops-onboarding.md     # This file
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kkarthee/azure_architect.git
cd azure_architect
git checkout devops/architecture-and-ppt
```

### 2. Configure Azure CLI

```bash
# Login to Azure
az login

# Set default subscription
az account set --subscription "<subscription-id>"

# Verify login
az account show
```

### 3. Configure Azure DevOps

```bash
# Install Azure DevOps extension
az extension add --name azure-devops

# Configure default organization and project
az devops configure --defaults organization=https://dev.azure.com/YourOrg project=YourProject
```

## CI/CD Pipeline

### Pipeline Overview

The Azure Pipeline (`pipelines/azure-pipelines.yml`) automates the following stages:

1. **Build**: Compile application and run tests
2. **Test**: Execute unit and integration tests
3. **Security Scan**: Run security and vulnerability checks
4. **Artifact**: Package and publish artifacts
5. **Deploy**: Deploy to target environments

### Running the Pipeline

The pipeline is triggered automatically on:
- Push to main branch
- Pull request creation
- Manual trigger

### Manual Pipeline Trigger

```bash
# Trigger pipeline using Azure CLI
az pipelines run --name "DevOps-Pipeline" --branch devops/architecture-and-ppt
```

## Infrastructure as Code

### Terraform Setup

1. **Initialize Terraform**:
```bash
cd iac/terraform
terraform init
```

2. **Review Configuration**:
```bash
terraform plan
```

3. **Apply Configuration**:
```bash
terraform apply
```

### Terraform Variables

Configure variables in `iac/terraform/variables.tf` or create a `terraform.tfvars` file:

```hcl
# terraform.tfvars
resource_group_name = "rg-devops-prod"
location           = "eastus"
environment        = "production"
```

### State Management

- Use Azure Storage for remote state
- Enable state locking
- Configure backend in `main.tf`

## Configuration Management

### Ansible Setup

1. **Update Inventory**:
Edit `iac/ansible/hosts` with your target hosts:
```ini
[web_servers]
webserver1.example.com
webserver2.example.com

[db_servers]
dbserver1.example.com
```

2. **Run Playbook**:
```bash
cd iac/ansible
ansible-playbook -i hosts deploy.yml
```

3. **Dry Run**:
```bash
ansible-playbook -i hosts deploy.yml --check
```

### Ansible Variables

Configure variables in `group_vars/` or `host_vars/` directories:

```yaml
# group_vars/web_servers.yml
app_port: 8080
app_user: appuser
app_path: /opt/myapp
```

## Security Practices

### Secret Management

- Store secrets in **Azure Key Vault**
- Reference secrets in pipelines using variable groups
- Never commit secrets to Git

### Service Principal

Create a service principal for automation:

```bash
az ad sp create-for-rbac --name "devops-sp" \
  --role contributor \
  --scopes /subscriptions/<subscription-id>
```

### RBAC Configuration

- Use least privilege principle
- Assign roles at appropriate scope
- Review and audit access regularly

### Security Scanning

The pipeline includes:
- Dependency vulnerability scanning
- Container image scanning
- Infrastructure security checks
- Code quality analysis

## Troubleshooting

### Common Issues

#### Terraform State Lock

```bash
# Force unlock (use with caution)
terraform force-unlock <lock-id>
```

#### Azure CLI Authentication

```bash
# Clear cached credentials
az account clear

# Re-authenticate
az login
```

#### Ansible Connection Issues

```bash
# Test connectivity
ansible all -i hosts -m ping

# Use verbose mode for debugging
ansible-playbook -i hosts deploy.yml -vvv
```

### Getting Help

- **Documentation**: Review architecture diagrams in `/diagrams`
- **Slides**: Check `/ppt/devops-architecture-slides.md` for detailed explanations
- **Support**: Contact the DevOps team via Azure DevOps boards

## Best Practices

1. **Version Control**: Commit all infrastructure and configuration code
2. **Code Review**: All changes require peer review via pull requests
3. **Testing**: Test changes in development before promoting to production
4. **Monitoring**: Monitor pipeline execution and deployment health
5. **Documentation**: Keep documentation up-to-date with changes
6. **Security**: Follow security best practices and compliance requirements

## Next Steps

1. Review the architecture diagram in `/diagrams/devops-architecture.svg`
2. Examine the presentation slides in `/ppt/devops-architecture-slides.md`
3. Explore the pipeline configuration in `/pipelines/azure-pipelines.yml`
4. Study the Terraform configurations in `/iac/terraform/`
5. Review Ansible playbooks in `/iac/ansible/`
6. Deploy to a development environment

## Resources

- [Azure DevOps Documentation](https://docs.microsoft.com/en-us/azure/devops/)
- [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Ansible Documentation](https://docs.ansible.com/)
- [Azure CLI Reference](https://docs.microsoft.com/en-us/cli/azure/)

---

**Happy DevOps Journey!** 🚀
