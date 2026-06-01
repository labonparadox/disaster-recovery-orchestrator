resource "azurerm_linux_virtual_machine" "vm_1" {
  admin_username      = var.admin_username
  location            = azurerm_resource_group.vm_rg.location
  name                = var.vm_name
  network_interface_ids = [azurerm_network_interface.az_nic.id]
  resource_group_name = azurerm_resource_group.vm_rg.name
  size                = var.vm_size

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    offer     = "0001-com-ubuntu-server-jammy"
    publisher = "Canonical"
    sku       = "22_04-lts"
    version   = "latest"
  }

  admin_ssh_key {
    public_key = tls_private_key.vm_ssh_key.public_key_openssh
    username   = var.admin_username
  }
}