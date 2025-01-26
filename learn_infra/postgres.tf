
resource "helm_release" "postgresql" {
  name       = "my-postgres"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql"

  create_namespace = true

  set {
    name  = "postgresqlPassword"
    value = var.postgres_password
  }

  set {
    name  = "postgresqlUsername"
    value = var.postgres_username
  }

  set {
    name  = "postgresqlDatabase"
    value = var.postgres_database
  }

  set {
    name  = "persistence.enabled"
    value = "false"
  }
}
