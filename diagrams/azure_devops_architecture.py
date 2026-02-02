

# Requires: pip install diagrams
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.devops import Boards, Repos, Pipelines, TestPlans
from diagrams.azure.security import KeyVaults, Sentinel, Defender
from diagrams.azure.compute import VM
from diagrams.azure.monitor import Monitor, ApplicationInsights, LogAnalyticsWorkspaces, AzureWorkbooks
# from diagrams.azure.general import Azure
from diagrams.azure.identity import ManagedIdentities
# from diagrams.azure.analytics import Synapse
from diagrams.azure.web import AppServices
from diagrams.onprem.iac import Terraform, Ansible
from diagrams.onprem.client import User
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.analytics import Tableau
from diagrams.saas.chat import Slack
# from diagrams.saas.collaboration import ServiceNow
from diagrams.saas.logging import Datadog
from diagrams.generic.database import SQL

# Optional: Add more imports for icons as needed

with Diagram("Azure DevOps Hybrid Architecture", show=False, filename="azure_devops_architecture_3", outformat="png", direction="LR"):
    user = User("Architect/Dev")

    with Cluster("On-Premises"):
        # sn = ServiceNow("ServiceNow")
        ans_onprem = Ansible("Ansible")
        tf_onprem = Terraform("Terraform")
        onprem_vm = VM("On-Prem VM")

    with Cluster("Azure DevOps"):
        boards = Boards("Azure Boards")
        repos = Repos("Azure Repos")
        pipelines = Pipelines("Azure Pipelines")
        testplans = TestPlans("Test Plans")
        sonar = Jenkins("SonarQube")
        kv = KeyVaults("Key Vault")
        tf = Terraform("Terraform")
        ans = Ansible("Ansible")
        python = AppServices("Python")
        automation = ManagedIdentities("Azure Automation")
        release = Pipelines("Release Pipelines")

    with Cluster("Environments"):
        dev = VM("Dev")
        # test = VM("Test")
        # stage = VM("Stage")
        preprod = VM("PreProd")
        prod = VM("Prod")

    with Cluster("Monitoring & Security"):
        log_analytics = LogAnalyticsWorkspaces("Log Analytics")
        app_insights = ApplicationInsights("App Insights")
        monitor = Monitor("Monitor Insight")
        workbooks = AzureWorkbooks("Workbooks")
        defender = Defender("Defender for Cloud")
        sentinel = Sentinel("Sentinel")
        # Sentinel AIOps, Portal Insight, Ops Insight, Service Map, etc. can be added as needed

    # Flows
  #  user >> sn
    user >> repos
   # sn >> boards
    repos >> pipelines
    pipelines >> sonar
    pipelines >> kv
    pipelines >> tf
    pipelines >> ans
    pipelines >> python
    pipelines >> automation
    pipelines >> testplans
    pipelines >> release
    pipelines >> defender
    pipelines >> log_analytics
    pipelines >> app_insights
    pipelines >> monitor
    pipelines >> workbooks
    pipelines >> sentinel
    pipelines >> dev
    # pipelines >> test
    # pipelines >> stage
    pipelines >> preprod
    pipelines >> prod

    # On-prem to cloud
    ans_onprem >> ans
    tf_onprem >> tf
    #tf >> [dev, test, stage, preprod, prod]
    # ans >> [dev, test, stage, preprod, prod]
    tf >> [dev, preprod, prod]
    ans >> [dev, preprod, prod]

    # Monitoring flows
    prod >> [app_insights, monitor, workbooks, defender, sentinel]
    dev >> [app_insights, monitor]
    # test >> [app_insights, monitor]
    # stage >> [app_insights, monitor]
    preprod >> [app_insights, monitor]

    # Feedback loops
    boards >> pipelines
    testplans >> boards
