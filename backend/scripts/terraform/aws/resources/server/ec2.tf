resource "aws_instance" "sample1" {

  ami = var.ami
  instance_type = var.vm_type
  key_name = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.security-grp1.id]

  tags = {
    Name = "ExampleInstance"
  }
}