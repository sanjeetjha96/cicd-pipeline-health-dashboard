variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "image_repo" {
  description = "Docker image repo for CI/CD dashboard app"
  type        = string
  default     = "your-dockerhub-username/cicd-dashboard:latest"
}

variable "db_enabled" {
  description = "Whether to create RDS Postgres"
  type        = bool
  default     = false
}

variable "db_name" {
  type    = string
  default = "dashboarddb"
}

variable "db_username" {
  type    = string
  default = "admin"
}

variable "db_password" {
  type    = string
  default = "password123"
}
