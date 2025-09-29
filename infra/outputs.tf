output "app_public_ip" {
  value = aws_instance.app.public_ip
}

output "rds_endpoint" {
  value       = try(aws_db_instance.dashboard_db[0].address, "")
  description = "RDS Postgres endpoint (if enabled)"
}
