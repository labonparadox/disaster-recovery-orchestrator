# outputs.tf - New file

output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.sample1.public_ip
}

output "instance_private_ip" {
  description = "Private IP of the EC2 instance"
  value       = aws_instance.sample1.private_ip
}

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.sample1.id
}

output "security_group_id" {
  description = "ID of the security group"
  value       = aws_security_group.security-grp1.id
}

output "key_name" {
  description = "Name of the key pair"
  value       = aws_key_pair.deployer.key_name
}