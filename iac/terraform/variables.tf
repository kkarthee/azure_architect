variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-devops"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "eastus"
}

variable "environment" {
  description = "Environment name (dev, staging, production)"
  type        = string
  default     = "dev"
  
  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production."
  }
}

variable "vnet_address_space" {
  description = "Address space for the virtual network"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "app_subnet_address_prefixes" {
  description = "Address prefixes for the application subnet"
  type        = list(string)
  default     = ["10.0.1.0/24"]
}

variable "app_service_sku" {
  description = "SKU for the App Service Plan"
  type        = string
  default     = "B1"
  
  validation {
    condition     = contains(["B1", "B2", "B3", "S1", "S2", "S3", "P1v2", "P2v2", "P3v2"], var.app_service_sku)
    error_message = "App Service SKU must be a valid Azure App Service plan SKU."
  }
}

variable "log_retention_days" {
  description = "Number of days to retain logs in Log Analytics"
  type        = number
  default     = 30
  
  validation {
    condition     = var.log_retention_days >= 30 && var.log_retention_days <= 730
    error_message = "Log retention days must be between 30 and 730."
  }
}

variable "common_tags" {
  description = "Common tags to apply to all resources"
  type        = map(string)
  default = {
    Project     = "Azure DevOps Architecture"
    ManagedBy   = "Terraform"
    Repository  = "azure_architect"
  }
}

variable "enable_monitoring" {
  description = "Enable monitoring and alerting"
  type        = bool
  default     = true
}

variable "enable_backup" {
  description = "Enable backup for resources"
  type        = bool
  default     = false
}

variable "allowed_ip_addresses" {
  description = "List of allowed IP addresses for Key Vault access"
  type        = list(string)
  default     = []
}

variable "app_settings" {
  description = "Additional application settings for the App Service"
  type        = map(string)
  default     = {}
}

variable "min_tls_version" {
  description = "Minimum TLS version for App Service"
  type        = string
  default     = "1.2"
}

variable "enable_https_only" {
  description = "Force HTTPS only for App Service"
  type        = bool
  default     = true
}
