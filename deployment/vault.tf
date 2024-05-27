variable "cloudflare_cert_path" {
  type        = string
  description = "Path to the Cloudflare certificate"
}

variable "cert_pass" {
  type        = string
  description = "Password for the certificate"
}

# Key Vault for secrets
data "azurerm_key_vault" "main_vault" {
  name = "fanta-nba-vault"
  #   location                   = data.azurerm_resource_group.main_group.location
  resource_group_name = data.azurerm_resource_group.main_group.name
  #   tenant_id                  = data.azurerm_client_config.current.tenant_id
  #   sku_name                   = "standard"
  #   access_policy {
  #     tenant_id = data.azurerm_client_config.current.tenant_id
  #     object_id = data.azurerm_client_config.current.object_id
  #
  #     certificate_permissions = [
  #       "Create",
  #       "Delete",
  #       "DeleteIssuers",
  #       "Get",
  #       "GetIssuers",
  #       "Import",
  #       "List",
  #       "ListIssuers",
  #       "ManageContacts",
  #       "ManageIssuers",
  #       "SetIssuers",
  #       "Update",
  #     ]
  #
  #     key_permissions = [
  #       "Backup",
  #       "Create",
  #       "Decrypt",
  #       "Delete",
  #       "Encrypt",
  #       "Get",
  #       "Import",
  #       "List",
  #       "Purge",
  #       "Recover",
  #       "Restore",
  #       "Sign",
  #       "UnwrapKey",
  #       "Update",
  #       "Verify",
  #       "WrapKey",
  #     ]
  #
  #     secret_permissions = [
  #       "Backup",
  #       "Delete",
  #       "Get",
  #       "List",
  #       "Purge",
  #       "Recover",
  #       "Restore",
  #       "Set",
  #     ]
  #   }
}

# data "azurerm_key_vault_certificate_data" "autoboost_cert" {
#   name         = "autoboost-cert"
#   key_vault_id = data.azurerm_key_vault.main_vault.id
# }

data "azurerm_key_vault_secret" "autoboost_cert" {
  name         = "autoboost-cert"
  key_vault_id = data.azurerm_key_vault.main_vault.id
}