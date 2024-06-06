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

output "env_default_domain" {
  value = azurerm_container_app_environment.app_env.default_domain
}

output "fqdn" {
  value = azurerm_container_app.container.ingress[0].fqdn
}

output "outbound_ip_addresses" {
  value = azurerm_container_app.container.outbound_ip_addresses
}

output "env_static_ip" {
  value = azurerm_container_app_environment.app_env.static_ip_address
}

output "container_custom_domain_name" {
  value = azurerm_container_app_custom_domain.custom_domain.name
}

output "managed_certificate_response" {
    value = azapi_resource.managed_certificate.output
}

output "custom_domain_binding_state_update_to_Disabled" {
    value = azapi_update_resource.custom_domain.output
}

output "custom_domain_binding_state_update_to_Enabled" {
    value = azapi_update_resource.custom_domain_binding.output
}


