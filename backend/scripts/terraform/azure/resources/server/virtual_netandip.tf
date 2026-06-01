resource "azurerm_virtual_network" "v_net" {
  address_space = var.address_space
  location            = azurerm_resource_group.vm_rg.location
  name                = var.virtual_net_name
  resource_group_name = azurerm_resource_group.vm_rg.name
}

resource "azurerm_subnet" "v_sub" {
  address_prefixes = var.sub_add
  name                 = "${var.vm_name}-subnet"
  resource_group_name  = azurerm_resource_group.vm_rg.name
  virtual_network_name = azurerm_virtual_network.v_net.name
}

resource "azurerm_public_ip" "vm_public_id" {
  name  = "${var.vm_name}-public_ip"
  location            = azurerm_resource_group.vm_rg.location
  allocation_method    = "Static"
  resource_group_name = azurerm_resource_group.vm_rg.name
}

resource "azurerm_network_interface" "az_nic" {
  location            = azurerm_resource_group.vm_rg.location
  name                = "${var.vm_name}-nic"
  resource_group_name = azurerm_resource_group.vm_rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id = azurerm_subnet.v_sub.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id = azurerm_public_ip.vm_public_id.id
  }
}