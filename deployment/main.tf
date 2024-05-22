# Microsoft Azure Provider configuration
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.104.0"
    }
  }
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
output "latest_revision_fqdn" {
  value = azurerm_container_app.container.latest_revision_fqdn
}

output "outbound_ip_addresses" {
  value = azurerm_container_app.container.outbound_ip_addresses
}

output "fqdn" {
  value = azurerm_container_app.container.ingress[0].fqdn
}

output "env_default_domain" {
  value = azurerm_container_app_environment.app_env.default_domain
}

output "env_static_ip" {
  value = azurerm_container_app_environment.app_env.static_ip_address
}
