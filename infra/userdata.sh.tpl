#!/bin/bash
yum update -y
amazon-linux-extras install docker -y
systemctl enable docker
systemctl start docker
usermod -aG docker ec2-user

# Run CI/CD Dashboard container
docker run -d -p 80:8080 ${image_repo}
