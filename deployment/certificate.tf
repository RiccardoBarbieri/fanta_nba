resource "time_sleep" "dns_propagation" {
  create_duration = "60s"

  depends_on = [azurerm_dns_txt_record.txt_autoboost, azurerm_dns_cname_record.cname_helloworld]

  triggers = {
    url = "${azurerm_dns_cname_record.cname_helloworld.name}.${data.azurerm_dns_zone.autoboost.name}",
  }
}


//see https://gist.github.com/fdelu/25f4eee056633abc03dc87b4a7e7704b
resource "azapi_update_resource" "custom_domain" {
  type        = "Microsoft.App/containerApps@2023-05-01"
  resource_id = azurerm_container_app.container.id

  body = jsonencode({
    properties = {
      configuration = {
        ingress = {
          customDomains = [
            {
              bindingType = "Disabled",
              name        = time_sleep.dns_propagation.triggers["url"],
            }
          ]
        }
      }
    }
  })

  response_export_values = ["*"]
}

resource "azapi_resource" "managed_certificate" {
  type = "Microsoft.App/ManagedEnvironments/managedCertificates@2024-03-01"

  name       = "hello-world-cert"
  parent_id  = azurerm_container_app_environment.app_env.id
  location   = data.azurerm_resource_group.main_group.location
  depends_on = [time_sleep.dns_propagation, azurerm_container_app_environment.app_env]

  body = jsonencode(
    {
      properties = {
        subjectName             = time_sleep.dns_propagation.triggers.url
        domainControlValidation = "CNAME"
      }
    }
  )

  response_export_values = ["*"]
}

resource "azapi_update_resource" "custom_domain_binding" {
  type        = "Microsoft.App/containerApps@2023-05-01"
  resource_id = azurerm_container_app.container.id

  body = jsonencode({
    properties = {
      configuration = {
        ingress = {
          customDomains = [
            {
              bindingType   = "SniEnabled",
              name          = time_sleep.dns_propagation.triggers["url"],
              certificateId = jsondecode(azapi_resource.managed_certificate.output).id
            }
          ]
        }
      }
    }
  })
  response_export_values = ["*"]
}