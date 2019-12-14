variable "environment" {
  default = "staging"
}

variable "secret" {}


output "secret" {
  value = "${var.secret}"
}
