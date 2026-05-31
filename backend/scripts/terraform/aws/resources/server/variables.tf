variable "ports" {
  type = list(number)
}
variable "cidr_blocks_ingress" {
  type = list(string)
}

variable "vm_type" {
  type = string
}

variable "ami" {
  type = string
}