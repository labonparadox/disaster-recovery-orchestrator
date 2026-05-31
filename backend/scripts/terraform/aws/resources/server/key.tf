resource "aws_key_pair" "deployer" {
  #  -key is must
  key_name = "deployer-key"
  public_key = tls_private_key.key.public_key_openssh

}

resource "tls_private_key" "key" {
  algorithm = "RSA"
  rsa_bits = 4096
}