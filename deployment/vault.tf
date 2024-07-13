# Key Vault for secrets
data "azurerm_key_vault" "main_vault" {
  name = "fanta-nba-vault"
  resource_group_name = data.azurerm_resource_group.main_group.name
}

data "azurerm_key_vault_secret" "odds_api_key" {
  name = "ODDS-API-KEY"
  key_vault_id = data.azurerm_key_vault.main_vault.id
}

data "azurerm_key_vault_secret" "cosmos_db_connection_string" {
  key_vault_id = data.azurerm_key_vault.main_vault.id
  name         = "COSMOSDB-CONNECTION-STRING"
}

data "azurerm_key_vault_secret" "cosmos_db_database" {
  key_vault_id = data.azurerm_key_vault.main_vault.id
  name         = "COSMOSDB-DATABASE"
}

data "azurerm_key_vault_secret" "docker_hub_password" {
  key_vault_id = data.azurerm_key_vault.main_vault.id
  name         = "DOCKER-HUB-PASSWORD"
}