# Requires: pip install diagrams
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.devops import Boards, Repos, Pipelines, TestPlans
from diagrams.azure.security import KeyVaults, Sentinel
from diagrams.azure.compute import VM
from diagrams.azure.monitor import Monitor, ApplicationInsights # LogAnalytics
from diagrams.onprem.vcs import Github
from diagrams.onprem.iac import Terraform, Ansible
from diagrams.onprem.client import User

# This script generates a 'hybrid_devops_architecture.png'
with Diagram("Hybrid DevOps Architecture", show=False, filename="hybrid_devops_architecture"):
    
    with Cluster("Planning"):
        plan = Boards("Azure Boards")
        code = Repos("Azure Repos")

    with Cluster("CI/CD Pipeline"):
        pipe = Pipelines("Azure Pipelines")
        kv = KeyVaults("Key Vault")
        tf = Terraform("Terraform")
        ans = Ansible("Ansible")
        
    with Cluster("Hybrid Infrastructure"):
        azure_vm = VM("Azure Cloud")
        on_prem = VM("On-Prem Server")
        
    with Cluster("Observability"):
        mon = Monitor("Azure Monitor")
        app_ins = ApplicationInsights("App Insights")
        sentinel = Sentinel("Azure Sentinel")

    # Flow
    plan >> code >> pipe
    pipe >> Edge(label="Secrets") >> kv
    pipe >> Edge(label="Provision") >> tf
    pipe >> Edge(label="Config") >> ans
    
    tf >> azure_vm
    tf >> on_prem
    ans >> azure_vm
    ans >> on_prem
    
    azure_vm >> mon
    on_prem >> mon
    azure_vm >> app_ins
    
    mon >> sentinel