terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.5.2"
    }
  }
}
resource "tls_private_key" "vm_ssh_key" {
  algorithm = "RSA"
  rsa_bits = 4096
}

resource "local_file" "private_key" {
  content = tls_private_key.vm_ssh_key.private_key_pem
  filename = pathexpand("~/.ssh/${var.vm_name}_key")
  file_permission = "0600"
}

resource "local_file" "public_key" {
  content = tls_private_key.vm_ssh_key.public_key_openssh
  filename = pathexpand("~/.ssh/${var.vm_name}_key".pem)
}