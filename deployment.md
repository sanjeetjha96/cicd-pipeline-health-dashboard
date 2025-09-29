# Deployment Guide – CI/CD Pipeline Health Dashboard (Cloud)

## Prerequisites
- AWS account + IAM user with EC2/VPC/RDS permissions
- AWS CLI installed & configured (`aws configure`)
- Terraform >= 1.5
- Docker image built & pushed (update `var.image_repo`)

## Steps

1. Clone the repo & go to infra:
   ```bash
   git clone https://github.com/your-org/cicd-pipeline-health-dashboard.git
   cd cicd-pipeline-health-dashboard/infra
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Review the plan:
   ```bash
   terraform plan -out=tfplan
   ```

4. Apply the infrastructure:
   ```bash
   terraform apply tfplan
   ```

5. Get app public IP:
   ```bash
   terraform output app_public_ip
   ```

6. Access the app:
   ```
   http://<PUBLIC_IP>
   ```

## Optional: Enable RDS
- In `terraform.tfvars` set:
  ```hcl
  db_enabled = true
  db_username = "admin"
  db_password = "your-secure-pass"
  ```
- Re-run `terraform apply`.

## Destroy Infra
```bash
terraform destroy
```
