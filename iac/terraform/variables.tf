variable "rg_name" {
  type        = string
  description = "Resource group name"
  default     = "devops-rg"
}

variable "location" {
  type        = string
  description = "Azure region"
  default     = "eastus"
}

variable "acr_name" {
  type        = string
  description = "ACR name (must be globally unique)"
  default     = "myacrdevops123"
}
