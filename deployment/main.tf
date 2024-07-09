# Microsoft Azure Provider configuration
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.104.0"
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

output "resource_group_name" {
  value = data.azurerm_resource_group.main_group.name
}

output "container_app_env_name" {
  value = azurerm_container_app_environment.app_env.name
}

output "custom_domain" {
  value = "helloworld.autoboost.it"
}

output "container_app_name" {
  value = azurerm_container_app.container.name
}

output "container_app_ip" {
  value = azurerm_container_app.container.outbound_ip_addresses[0]
}
