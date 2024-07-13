# App environment
data "azurerm_container_app_environment" "app_env" {
  name                = "fantanba-env"
  resource_group_name = data.azurerm_resource_group.main_group.name
}

# resource "azurerm_container_app_environment" "app_env" {
#   name                       = "fantanba-env"
#   location                   = "West Europe"
#   resource_group_name        = data.azurerm_resource_group.main_group.name
#   log_analytics_workspace_id = azurerm_log_analytics_workspace.example.id
# }
#
# resource "azurerm_log_analytics_workspace" "example" {
#   name                = "logs"
#   location            = data.azurerm_resource_group.main_group.location
#   resource_group_name = data.azurerm_resource_group.main_group.name
#   sku                 = "PerGB2018"
#   retention_in_days   = 30
# }

# Substituted custom domain with the custom script
# See gist https://gist.github.com/LynnAU/131426847d2793c76e36548f9937f966
# Track issue https://github.com/hashicorp/terraform-provider-azurerm/issues/25788 for updates

variable "bet-api-target-port" {
  description = "Port for the bet-api service"
  type        = number
}

# Template https://learn.microsoft.com/en-us/azure/templates/microsoft.app/containerapps?pivots=deployment-language-terraform#ingress-2

# resource "azapi_resource" "bet_api" {
#   type      = "Microsoft.App/containerApps@2023-11-02-preview"
#   name      = "bet-api"
#   location  = data.azurerm_resource_group.main_group.location
#   parent_id = data.azurerm_resource_group.main_group.id
#
#   identity {
#     type = "SystemAssigned"
#   }
#
#   body = jsonencode({
#     properties = {
#       configuration = {
#         activeRevisionsMode = "Single"
#         ingress = {
#           allowInsecure        = true
#           clientCertificateMode = "ignore"
#           #           exposedPort            = 80 TODO maybe specify (or is it default?)
#           external             = true
#           targetPort           = var.bet-api-target-port
#           targetPortHttpScheme = "http"
#           traffic              = [
#             {
#               latestRevision = true
#               weight         = 100
#             }
#           ]
#           transport = "http"
#         }
#         maxInactiveRevisions = 2
#         registries           = [
#           {
#             #             identity          = "string"
#             passwordSecretRef = "registry-password"
#             server            = data.azurerm_container_registry.main_registry.login_server
#             username          = data.azurerm_container_registry.main_registry.admin_username
#           }
#         ]
#         secrets = [
#           {
#             name  = lower(data.azurerm_key_vault_secret.odds_api_key.name)
#             value = data.azurerm_key_vault_secret.odds_api_key.value
#           },
#           {
#             name  = lower(data.azurerm_key_vault_secret.cosmos_db_connection_string.name)
#             value = data.azurerm_key_vault_secret.cosmos_db_connection_string.value
#           },
#           {
#             name  = lower(data.azurerm_key_vault_secret.cosmos_db_database.name)
#             value = data.azurerm_key_vault_secret.cosmos_db_database.value
#           },
#           {
#             name  = "registry-password"
#             value = data.azurerm_container_registry.main_registry.admin_password
#           }
#         ]
#       }
#       environmentId = data.azurerm_container_app_environment.app_env.id
#       template = {
#         containers = [
#           {
#             env = [
#               {
#                 name      = "ODDS_API_KEY"
#                 secretRef = lower(data.azurerm_key_vault_secret.odds_api_key.name)
#               },
#               {
#                 name      = "COSMOSDB_CONNECTION_STRING"
#                 secretRef = lower(data.azurerm_key_vault_secret.cosmos_db_connection_string.name)
#               },
#               {
#                 name      = "COSMOSDB_DATABASE"
#                 secretRef = lower(data.azurerm_key_vault_secret.cosmos_db_database.name)
#               }
#             ]
#             image = "${data.azurerm_container_registry.main_registry.login_server}/fantanba/bet_api:latest"
#             name  = "bet-api-image"
#             resources = {
#               cpu    = 1
#               memory = "2Gi"
#             }
#           }
#         ]
#         scale = {
#           maxReplicas = 10
#           minReplicas = 1
#           rules       = [
#             {
#               name = "http-scale-rule"
#               http = {
#                 metadata = {
#                   concurrentRequests = "20"
#                 }
#               }
#             }
#           ]
#         }
#       }
#     }
#   })
# }


resource "azurerm_container_app" "bet_api" {
  name                         = "bet-api"
  container_app_environment_id = data.azurerm_container_app_environment.app_env.id
  resource_group_name          = data.azurerm_resource_group.main_group.name
  revision_mode                = "Single"

  identity {
    type = "SystemAssigned"
  }

  secret {
    name  = "registry-password"
    value = data.azurerm_container_registry.main_registry.admin_password
  }

  secret {
    name  = lower(data.azurerm_key_vault_secret.odds_api_key.name)
    value = data.azurerm_key_vault_secret.odds_api_key.value
  }

  secret {
    name  = lower(data.azurerm_key_vault_secret.cosmos_db_connection_string.name)
    value = data.azurerm_key_vault_secret.cosmos_db_connection_string.value
  }

  secret {
    name  = lower(data.azurerm_key_vault_secret.cosmos_db_database.name)
    value = data.azurerm_key_vault_secret.cosmos_db_database.value
  }

  registry {
    server               = data.azurerm_container_registry.main_registry.login_server
    username             = data.azurerm_container_registry.main_registry.admin_username
    password_secret_name = "registry-password"
  }

  template {
    min_replicas = 1
    max_replicas = 5

    # Total CPU and memory for all containers defined in a Container App must add up to one of the following CPU - Memory combinations: [cpu: 0.25, memory: 0.5Gi]; [cpu: 0.5, memory: 1.0Gi]; [cpu: 0.75, memory: 1.5Gi]; [cpu: 1.0, memory: 2.0Gi]; [cpu: 1.25, memory: 2.5Gi]; [cpu: 1.5, memory: 3.0Gi]; [cpu: 1.75, memory: 3.5Gi]; [cpu: 2.0, memory: 4.0Gi]
    container {

      image  = "${data.azurerm_container_registry.main_registry.login_server}/fantanba/bet_api:latest"
      memory = "2Gi"
      cpu    = 1
      name   = "bet-api-image"

      env {
        name        = "ODDS_API_KEY"
        secret_name = lower(data.azurerm_key_vault_secret.odds_api_key.name)
      }

      env {
        name        = "COSMOSDB_CONNECTION_STRING"
        secret_name = lower(data.azurerm_key_vault_secret.cosmos_db_connection_string.name)
      }

      env {
        name        = "COSMOSDB_DATABASE"
        secret_name = lower(data.azurerm_key_vault_secret.cosmos_db_database.name)
      }
    }

    http_scale_rule {
      concurrent_requests = 20
      name                = "http-scale-rule"
    }
  }

  ingress {
    external_enabled = true
    target_port      = var.bet-api-target-port
    transport        = "http"
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}