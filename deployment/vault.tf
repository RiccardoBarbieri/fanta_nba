# variable "cloudflare_cert_path" {
#   type        = string
#   description = "Path to the Cloudflare certificate"
# }

# Key Vault for secrets
data "azurerm_key_vault" "main_vault" {
  name = "fanta-nba-vault"
  resource_group_name = data.azurerm_resource_group.main_group.name
}