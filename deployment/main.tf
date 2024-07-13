# Microsoft Azure Provider configuration
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.111.0"
    }
    azapi = {
      source  = "azure/azapi"
      version = "=1.13.1"
    }
  }
}

provider "azapi" {
}

provider "azurerm" {
  skip_provider_registration = true
  features {
    key_vault {
      purge_soft_delete_on_destroy               = true
      purge_soft_deleted_certificates_on_destroy = true
      purge_soft_deleted_keys_on_destroy         = true
    }
  }
}

# Data source to get the EXISTING resource group
data "azurerm_resource_group" "main_group" {
  name = "srs2024-stu-g13"
}

data "azurerm_client_config" "current" {}


# _____________________________________________________________
# OUTPUTS

output "container_app_id" {
  value = azurerm_container_app.bet_api.id
}

output "container_app_identity" {
  value = azurerm_container_app.bet_api.identity
}