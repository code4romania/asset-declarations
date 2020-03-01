resource "aws_security_group" "public" {
  name        = "${local.prefix}-public"
  description = "Public access"
  vpc_id      = aws_vpc.app.id
  tags = {
    Name = "${local.prefix}-public"
  }
}

resource "aws_security_group" "intra" {
  name        = "${local.prefix}-intra"
  description = "Intra-service access. Used for App-DB communication."
  vpc_id      = aws_vpc.app.id
  tags = {
    Name = "${local.prefix}-intra"
  }
}

resource "aws_security_group_rule" "public" {
  description       = "Give public access on HTTP"
  security_group_id = aws_security_group.public

  cidr_blocks = "0.0.0.0/0"
  from_port   = 80
  to_port     = 80
  protocol    = "tcp"
  type        = "ingress"
}

resource "aws_security_group_rule" "intra" {
  description       = "Allow intra-service communication"
  security_group_id = aws_security_group.intra

  from_port = -1
  to_port   = -1
  protocol  = "all"
  type      = "ingress"
  self      = true
}
