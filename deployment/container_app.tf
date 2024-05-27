# App environment
resource "azurerm_container_app_environment" "app_env" {
  name                = "HelloWorld-Environment"
  location            = data.azurerm_resource_group.main_group.location
  resource_group_name = data.azurerm_resource_group.main_group.name
}

resource "azurerm_container_app_environment_certificate" "env_cert" {
  certificate_blob_base64      = base64encode(data.azurerm_key_vault_secret.autoboost_cert.value)
#   certificate_blob_base64      = base64encode(format("%s%s", data.azurerm_key_vault_certificate_data.autoboost_cert.pem, data.azurerm_key_vault_certificate_data.autoboost_cert.key))
  certificate_password         = ""
  container_app_environment_id = azurerm_container_app_environment.app_env.id
  name                         = "env-cert"

  depends_on = [
    data.azurerm_key_vault_secret.autoboost_cert
  ]
}

resource "azurerm_container_app_custom_domain" "custom_domain" {
  name                                     = trimprefix(azurerm_dns_txt_record.txt_autoboost.fqdn, "asuid.")
  container_app_id                         = azurerm_container_app.container.id
  container_app_environment_certificate_id = azurerm_container_app_environment_certificate.env_cert.id
  certificate_binding_type                 = "SniEnabled"


  depends_on = [
    azurerm_dns_cname_record.cname_helloworld,
    azurerm_dns_txt_record.txt_autoboost
  ]
}

# App container
resource "azurerm_container_app" "container" {
  name                         = "hello-world"
  container_app_environment_id = azurerm_container_app_environment.app_env.id
  resource_group_name          = data.azurerm_resource_group.main_group.name
  revision_mode                = "Single"

  template {
    min_replicas = 1
    max_replicas = 2
    container {
      name   = "hello-world-image"
      image  = "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest"
      cpu    = 0.25
      memory = "0.5Gi"
    }
  }

  ingress {
    external_enabled = true
    target_port      = 80
    transport        = "http"
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }

#   depends_on = [
#     azurerm_dns_cname_record.cname_autoboost,
#     azurerm_dns_txt_record.txt_autoboost
#   ]
}