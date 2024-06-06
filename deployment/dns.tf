

# locals {
#   input_string = "hello-world--1k7gmlj.kindgrass-b69cf8c6.westeurope.azurecontainerapps.io"
# #   input_string = azurerm_container_app.container.latest_revision_fqdn
#   before_rev = split("--", local.input_string)[0]
#   after_rev = index(local.input_string, ".")
# #   after_rev = slice(split(".", local.input_string), 1, length(split(".", local.input_string)) - 1)
#
#   fqdn = join(".", [local.before_rev, local.after_rev])
#
# }

# output "fqdn" {
#   value = local.fqdn
# }

data "azurerm_dns_zone" "autoboost" {
  name                = "autoboost.it"
  resource_group_name = data.azurerm_resource_group.main_group.name
}

resource "azurerm_dns_cname_record" "cname_helloworld" {
  name                = "helloworld"
  zone_name           = data.azurerm_dns_zone.autoboost.name
  resource_group_name = data.azurerm_dns_zone.autoboost.resource_group_name
  ttl                 = 60
  record              = azurerm_container_app.container.ingress[0].fqdn

}

resource "azurerm_dns_txt_record" "txt_autoboost" {
  name                = "asuid.helloworld"
  zone_name           = data.azurerm_dns_zone.autoboost.name
  resource_group_name = data.azurerm_dns_zone.autoboost.resource_group_name
  ttl                 = 60

  record {
    value = azurerm_container_app_environment.app_env.custom_domain_verification_id
  }
}