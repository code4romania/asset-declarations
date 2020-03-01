locals {
  subnet_count_app    = 1
  subnet_count_public = 2
  subnet_count_db     = 2
}

data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "app" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = local.prefix
  }
}

output "VPC CIDR" {
  value = aws_vpc.app.cidr_block
}

#################################################
# Subnets
#################################################

resource "aws_subnet" "public" {
  count             = local.subnet_count_public
  vpc_id            = aws_vpc.app.id
  cidr_block        = cidrsubnet(aws_vpc.app.cidr_block, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${local.prefix}-public"
  }
}

output "Subnet Public CIDR" {
  value = aws_subnet.public.*.cidr_block
}

resource "aws_subnet" "private-app" {
  count             = local.subnet_count_app
  vpc_id            = aws_vpc.app.id
  cidr_block        = cidrsubnet(aws_vpc.app.cidr_block, 8, local.subnet_count_public + count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${local.prefix}-private-app"
  }
}

output "Subnet Private App CIDR" {
  value = aws_subnet.private-app.*.cidr_block
}

resource "aws_subnet" "private-db" {
  count             = local.subnet_count_db
  vpc_id            = aws_vpc.app.id
  cidr_block        = cidrsubnet(aws_vpc.app.cidr_block, 8, local.subnet_count_public + local.subnet_count_app + count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${local.prefix}-private-db"
  }
}

output "Subnet Private DB CIDR" {
  value = aws_subnet.private-db.*.cidr_block
}

#################################################
# Gateways
#################################################

resource "aws_internet_gateway" "public" {
  vpc_id = aws_vpc.app.id

  tags = {
    Name = "${local.prefix}-public"
  }
}

resource "aws_eip" "private" {
  vpc = true

  tags = {
    Name = "${local.prefix}-private-app"
  }
}

output "NAT Egress Elastic IP" {
  value = aws_eip.private.private_ip
}

resource "aws_nat_gateway" "private" {
  allocation_id = aws_eip.private.id
  subnet_id     = element(aws_subnet.public.*.id, 0)

  tags = {
    Name = "${local.prefix}-private-app"
  }
}

#################################################
# Route tables
#################################################

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.app.id

  tags = {
    Name = "${local.prefix}-public"
  }
}

resource "aws_route_table" "private-app" {
  vpc_id = aws_vpc.app.id

  tags = {
    Name = "${local.prefix}-private-app"
  }
}

resource "aws_route_table" "private-db" {
  vpc_id = aws_vpc.app.id

  tags = {
    Name = "${local.prefix}-private-db"
  }
}

#################################################
# Routes
#################################################

resource "aws_route_table_association" "public-gw" {
  route_table_id = aws_route_table.public.id
  gateway_id     = aws_internet_gateway.public.id
}

resource "aws_route_table_association" "private-gw" {
  route_table_id = aws_route_table.private-app.id
  gateway_id     = aws_nat_gateway.private.id
}

resource "aws_route_table_association" "public" {
  count          = local.subnet_count_public
  route_table_id = aws_route_table.private-app.id
  subnet_id      = element(aws_subnet.public.*.id, count.index)
}

resource "aws_route_table_association" "private-app" {
  count          = local.subnet_count_app
  route_table_id = aws_route_table.private-app.id
  subnet_id      = element(aws_subnet.private-app.*.id, count.index)
}

resource "aws_route_table_association" "private-db" {
  count          = local.subnet_count_db
  route_table_id = aws_route_table.private-db.id
  subnet_id      = element(aws_subnet.private-db.*.id, count.index)
}
