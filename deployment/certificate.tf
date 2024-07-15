variable "services" {
  type = list(object({
    key = string
    custom_domain = string
    container_app_name = string
  }))
}


resource "null_resource" "null" {
  for_each = { for svc in var.services : svc.key => svc }

  lifecycle {
    create_before_destroy = false
  }

  triggers = {
    rg_name       = data.azurerm_resource_group.main_group.name
    ca_env_name   = data.azurerm_container_app_environment.app_env.name
    custom_domain = each.value.custom_domain
    ca_name       = each.value.container_app_name
    # Added to give chage to state between runs
    ca_ip         = azurerm_container_app.bet_api.outbound_ip_addresses[0]
  }

  # provision a managed cert and apply it to the container app
  provisioner "local-exec" {
    when    = create
    command = "bash ${path.module}/scripts/create.sh"

    environment = {
      RESOURCE_GROUP         = self.triggers.rg_name
      CONTAINER_APP_ENV_NAME = self.triggers.ca_env_name
      CUSTOM_DOMAIN          = self.triggers.custom_domain
      CONTAINER_APP_NAME     = self.triggers.ca_name
    }
  }

  provisioner "local-exec" {
    when    = destroy
    command = "bash ${path.module}/scripts/destroy.sh"

    environment = {
      RESOURCE_GROUP         = self.triggers.rg_name
      CONTAINER_APP_ENV_NAME = self.triggers.ca_env_name
      CUSTOM_DOMAIN          = self.triggers.custom_domain
      CONTAINER_APP_NAME     = self.triggers.ca_name
    }
  }
}
