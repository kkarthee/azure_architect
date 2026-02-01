# Title Slide
Title: Hybrid DevOps Architecture — Azure + On‑Prem
Subtitle: CI/CD, IaC, Observability, and Security
Author: kkarthee
Date: 2026-02-01
---
# Executive Summary
- Goal: Reliable, secure hybrid DevOps platform spanning on‑prem and Azure.
- Benefits: standardized IaC (Terraform), repeatable configs (Ansible), centralized telemetry (Log Analytics, App Insights), security (Defender & Sentinel).
Speaker notes:
This deck presents a mid-level architecture for a hybrid environment targeting architects. It shows CI/CD, IaC, configuration management, monitoring, and security integration.

---
# Goals & Non-functional Requirements
- Environments: dev, test, stage, preprod, prod
- RTO/RPO targets, compliance, encryption in transit & at rest
- RBAC via Azure AD, least privilege for pipelines
Speaker notes:
Define SLA/Compliance expectations early. Use RBAC and managed identities for safe secret access.

---
# High-Level Architecture (Diagram)
- Visual: Architecture SVG included (diagrams/devops-architecture.svg)
- Key layers: Dev & Planning → CI/CD → Infra / Runtime (On‑Prem + Azure) → Observability & Security
Speaker notes:
Walk through main flows: commit → pipeline → terraform → ansible → runtime → telemetry → sentinel.

---
# CI / Build Pipeline
- Azure Pipelines triggers on PRs and merges
- SonarQube for static analysis and quality gates
- Build artifacts: container images pushed to ACR
Speaker notes:
Quality gates enforce standards pre-merge; pipelines handle builds, tests, scans and artifact publishing.

---
# Infrastructure: Terraform
- Terraform modules for network, AKS/VMs, ACR, Key Vault, Log Analytics
- State stored in secure Azure Storage with locks and RBAC
Speaker notes:
Recommend modular design with environment workspaces and remote state secured with SAS + RBAC.

---
# Configuration & Deployment: Ansible
- Ansible for VM configuration, package installs, service management, and application deployment on both on‑prem and cloud.
- Use pipeline tasks to run Ansible playbooks with secrets from Key Vault.
Speaker notes:
Use inventories per environment (dev/test/...), and AWX/Tower only if centralized UI needed.

---
# Secrets & Credential Management
- Azure Key Vault for secrets and certs
- Pipelines use managed identity or service principal with limited access
Speaker notes:
Avoid inline secrets; use Key Vault-backed pipeline variables or task-based retrieval.

---
# Observability & Monitoring
- App telemetry → Application Insights
- Container & host logs → Log Analytics (Container Insights)
- Dashboards & Workbooks for analytics and runbooks
Speaker notes:
Define standard telemetry context and sampling levels for consistent analysis.

---
# Security & SIEM
- Defender for Cloud for posture & workload protection
- Azure Sentinel ingests logs from Log Analytics & App Insights
- Playbooks for automated remediation and ServiceNow integration
Speaker notes:
Sentinel playbooks connect to ServiceNow for incident creation and to Automation runbooks for remediation.

---
# Release Strategy & Environments
- Branching and promotion: feature → dev → test → stage → preprod → prod
- Approvals and deployment gates in release pipelines
Speaker notes:
Leverage approvals and automatic smoke tests before promotion.

---
# Testing Strategy
- Unit tests, integration tests, and automated acceptance tests
- Azure Test Plans for manual/ exploratory tests as needed
Speaker notes:
Shift-left testing and include synthetic tests post-deploy to validate telemetry flows.

---
# Automation & Remediation
- Azure Automation runbooks and Sentinel playbooks for auto-remediation
- Ansible for config drift remediation
Speaker notes:
Define actionable alerts and playbooks; keep remediation idempotent and safe for production.

---
# Operational Runbook
- Alerting flow: Monitor → Pager/Teams → On-call → ServiceNow ticket
- Runbook includes triage steps and expected MTTR
Speaker notes:
Include runbook links in dashboards for quick action.

---
# Roadmap & Next Steps
- Pilot: dev & test using AKS + one on‑prem app
- Phase 2: full rollout, integrate ServiceNow, tune Sentinel rules
- Phase 3: AIOps tuning and additional automation
Speaker notes:
Suggest a 3-phase rollout with measurable KPIs.

---
# Appendix — Starter YAML & IaC
- Azure Pipelines YAML: pipelines/azure-pipelines.yml
- Terraform skeleton: iac/terraform/*
- Ansible skeleton: iac/ansible/*
Speaker notes:
Use the appendix artifacts as a starting point for implementation.
