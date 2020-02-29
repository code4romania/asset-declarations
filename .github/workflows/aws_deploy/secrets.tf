resource "aws_ssm_parameter" "db_username" {
  name   = "/${local.prefix}/db_username"
  value  = var.db_username
  type   = "SecureString"
  key_id = aws_kms_key.main.id

  tags = {
    Name = local.prefix
  }
}

resource "aws_ssm_parameter" "db_password" {
  name   = "/${local.prefix}/db_password"
  value  = var.db_password
  type   = "SecureString"
  key_id = aws_kms_key.main.id

  tags = {
    Name = local.prefix
  }
}

resource "aws_kms_key" "main" {
  description = "Key for ${local.prefix} for secret variables"
  tags = {
    Name = local.prefix
  }
}
