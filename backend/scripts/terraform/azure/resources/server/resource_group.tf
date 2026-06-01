resource "azurerm_resource_group" "vm_rg" {
  location = var.resorce_group_loaction
  name     = var.resource_group_name
}