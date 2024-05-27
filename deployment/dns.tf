data "azurerm_dns_zone" "autoboost" {
  name                = "autoboost.it"
  resource_group_name = data.azurerm_resource_group.main_group.name
}

resource "azurerm_dns_cname_record" "cname_helloworld" {
  name = "helloworld"
  #   name                = "helloworld.autoboost.it"
  zone_name           = data.azurerm_dns_zone.autoboost.name
  resource_group_name = data.azurerm_dns_zone.autoboost.resource_group_name
  ttl                 = 300
  record              = azurerm_container_app.container.latest_revision_fqdn

  #   target_resource_id =
}

resource "azurerm_dns_a_record" "example" {
  name                = "test"
  zone_name           = data.azurerm_dns_zone.autoboost.name
  resource_group_name = data.azurerm_dns_zone.autoboost.resource_group_name
  ttl                 = 300
  records             = [azurerm_container_app.container.outbound_ip_addresses[0]]
}



resource "azurerm_dns_txt_record" "txt_autoboost" {
  name                = "asuid.helloworld"
  zone_name           = data.azurerm_dns_zone.autoboost.name
  resource_group_name = data.azurerm_dns_zone.autoboost.resource_group_name
  ttl                 = 300

  record {
    #     value = .properties.customDomainConfiguration.customDomainVerificationId
    value = azurerm_container_app_environment.app_env.custom_domain_verification_id
  }
}

# resource "azurerm_dns_cname_record" "hello-world" {
#   name                = "hello-world"
#   zone_name           = azurerm_dns_zone.riccardob.name
#   resource_group_name = data.azurerm_resource_group.main_group.name
#   ttl                 = 300
#   record              = "riccardob.dev"
# }