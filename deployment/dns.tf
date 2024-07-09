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