resource "aws_instance" "app" {
  ami           = "ami-0f58b397bc5c1f2e8" # Amazon Linux 2 in ap-south-1
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  user_data = templatefile("${path.module}/userdata.sh.tpl", {
    image_repo = var.image_repo
  })

  tags = {
    Name = "ci-cd-dashboard"
  }
}
