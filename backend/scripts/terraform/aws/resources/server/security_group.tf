resource "aws_security_group" "security-grp1" {
  name = "for_tf"

  dynamic "ingress" {
    for_each = var.ports
    iterator = ports
    content {
      description = "ports"
      from_port = ports.value
      to_port = ports.value
      protocol = "tcp"
      cidr_blocks = var.cidr_blocks_ingress
    }
  }

  dynamic "engress" {
    for_each = var.ports
    iterator = ports
    content {

      description = "ports"
      from_port = ports.value
      to_port = ports.value
      protocol = "tcp"
      cidr_blocks = var.cidr_blocks_ingress

    }
  }
}