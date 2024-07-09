# App environment
resource "azurerm_container_app_environment" "app_env" {
  name                = "HelloWorld-Environment"
  location            = data.azurerm_resource_group.main_group.location
  resource_group_name = data.azurerm_resource_group.main_group.name
}

# Substituted by the custom script
# See gist https://gist.github.com/LynnAU/131426847d2793c76e36548f9937f966
# Track issue https://github.com/hashicorp/terraform-provider-azurerm/issues/25788 for updates
# resource "azurerm_container_app_custom_domain" "custom_domain" {
#   name             = "helloworld.autoboost.it"
#   container_app_id = azurerm_container_app.container.id
#
#   depends_on = [
#     azurerm_dns_cname_record.cname_helloworld,
#     azurerm_dns_txt_record.txt_autoboost
#   ]
# }

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
}