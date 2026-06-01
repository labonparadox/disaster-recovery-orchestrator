variable "resorce_group_loaction" {
  type = string

}

variable "resource_group_name" {

  type = string

}

variable "vm_name" {
  type = string

}

variable "vm_size" {
  type = string
  default = "Standard_B1s"
}

variable "address_space" {
  type = list(string)
}

variable "virtual_net_name" {
  type = string
}

variable "sub_add" {
  type = list(string)
}

variable "admin_username" {
  type = string
}
