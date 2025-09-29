**Prompt 1:**  
"Write Terraform code to provision an EC2 instance in AWS with Docker installed and run a container from my custom image."  
**Output:**  
Generated `ec2.tf` + `userdata.sh.tpl`.

**Prompt 2:**  
"Add networking basics: VPC, subnet, Internet Gateway, and route table for public access."  
**Output:**  
Generated `networking.tf`.

**Prompt 3:**  
"Create security group for SSH + HTTP access."  
**Output:**  
Generated `security.tf`.

**Prompt 4:**  
"Add optional RDS Postgres database, enabled with a variable."  
**Output:**  
Generated `rds.tf`.

**Prompt 5:**  
"Write a step-by-step Deployment Guide (deployment.md)."  
**Output:**  
Produced Terraform usage documentation.

✅ This demonstrates AI-native workflow for Infrastructure-as-Code.
