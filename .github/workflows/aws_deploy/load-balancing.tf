resource "aws_alb" "main" {
  load_balancer_type = "application"
  name               = local.prefix
  subnets            = aws_subnet.public.*.id
  tags = {
    Name = local.prefix
  }
}

output "Load-Balancer DNS" {
  value = aws_alb.main.dns_name
}

resource "aws_alb_listener" "main" {
  load_balancer_arn = aws_alb.main.arn
  port              = 80

  default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.main.id
  }
}

resource "aws_alb_target_group" "main" {
  name   = local.prefix
  vpc_id = aws_vpc.app.id

  tags = {
    Name = local.prefix
  }
}
