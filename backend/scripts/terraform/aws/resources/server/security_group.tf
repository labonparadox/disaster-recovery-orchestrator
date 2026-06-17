resource "aws_security_group" "security-grp1" {
  name = "for_tf"
  description = "Security group for Terraform managed resources"

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

  dynamic "egress" {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    
  }
}