resource "aws_db_instance" "main" {
  name           = local.prefix
  engine         = "postgres"
  engine_version = "11.6"
  instance_class = "db.t2.micro"

  allocated_storage       = 10
  apply_immediately       = true
  backup_retention_period = 5
  db_subnet_group_name    = aws_db_subnet_group.main.name
  multi_az                = true
  skip_final_snapshot     = true
  vpc_security_group_ids  = [aws_security_group.intra.id]

  username = aws_ssm_parameter.db_username.value
  password = aws_ssm_parameter.db_password.value

  tags = {
    Name = local.prefix
  }
}

resource "aws_db_subnet_group" "main" {
  name       = local.prefix
  subnet_ids = aws_subnet.private-db.*.id
  tags = {
    Name = local.prefix
  }
}
