locals {
  container_name = "catpol"
  container_port = 8000
}

resource "aws_ecs_cluster" "app" {
  name = local.prefix

  tags = {
    Name = local.prefix
  }
}

resource "aws_ecs_service" "app" {
  name            = local.prefix
  cluster         = aws_ecs_cluster.app.id
  task_definition = aws_ecs_task_definition.app.id
  desired_count   = 1
  launch_type     = "FARGATE"
  #   iam_role =
  #   depends_on = []

  load_balancer {
    target_group_arn = aws_alb_target_group.main.id
    container_name   = local.container_name
    container_port   = local.container_port
  }
}

resource "aws_ecs_task_definition" "app" {
  family                   = local.prefix
  container_definitions    = data.template_file.task-def.rendered
  requires_compatibilities = ["FARGATE"]
  cpu                      = 1
  memory                   = 1024
}

data "template_file" "task-def" {
  template = file("task-def_template.json")
  vars = {
    container_name  = local.container_name
    container_port  = local.container_port
    container_image = var.docker_image

    db_username = aws_ssm_parameter.db_username.value
    db_password = aws_ssm_parameter.db_password.value
  }
}
