data "azurerm_container_registry" "main_registry" {
  name                = "fantanbareg"
  resource_group_name = data.azurerm_resource_group.main_group.name
}