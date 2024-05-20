terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.104.0"
    }
  }
}

variable "mock_api_key" {
    type = string
}

# Microsoft Azure Provider configuration
provider "azurerm" {
  skip_provider_registration = true
  features {
    key_vault {
      purge_soft_delete_on_destroy = true
      recover_soft_deleted_keys    = true
    }
  }
}

# Data source to get the EXISTING resource group
data "azurerm_resource_group" "main_group" {
  name = "srs2024-stu-g13"
}

data "azurerm_client_config" "current" {}

# App environment
resource "azurerm_container_app_environment" "app_env" {
  name                = "Example-Environment"
  location            = data.azurerm_resource_group.main_group.location
  resource_group_name = data.azurerm_resource_group.main_group.name
}

# Key Vault for secrets
resource "azurerm_key_vault" "main_vault" {
  name                = "deception-core-kv2"
  location            = data.azurerm_resource_group.main_group.location
  resource_group_name = data.azurerm_resource_group.main_group.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"
  #   soft_delete_retention_days = 7

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    key_permissions = [
      "Create",
      "Get",
      "List",
      "Purge",
    ]

    secret_permissions = [
      "Set",
      "Get",
      "Delete",
      "Recover",
      "List",
      "Purge",
    ]
  }
}

# SECRETS
resource "azurerm_key_vault_secret" "mockaroo_api_key" {
  name         = "MOCKAROO-API-KEY"
  value        = var.mock_api_key
  key_vault_id = azurerm_key_vault.main_vault.id
}

# App container
resource "azurerm_container_app" "container" {
  name                         = "deception-core"
  container_app_environment_id = azurerm_container_app_environment.app_env.id
  resource_group_name          = data.azurerm_resource_group.main_group.name
  revision_mode                = "Single"

  secret {
    name = "mockaroo-api-key"
    value = azurerm_key_vault_secret.mockaroo_api_key.value
  }

  template {
    min_replicas = 1
    max_replicas = 2
    container {
      name   = "deception-core-container"
      image  = "riccardoob/deception-core:latest"
      cpu    = 0.25
      memory = "0.5Gi"
      env {
        name  = "MOCKAROO_API_KEY"
        secret_name = "mockaroo-api-key"
      }
    }
  }

  ingress {
    external_enabled = true
    allow_insecure_connections = true
    #     exposed_port               = 8015
    target_port      = 8015
    transport        = "http"
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}

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
