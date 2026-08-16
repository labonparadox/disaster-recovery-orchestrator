resource "azurerm_resource_group" "vm_rg" {
  location = var.resource_group_location
  name     = var.resource_group_name
}