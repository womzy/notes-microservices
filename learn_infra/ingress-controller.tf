resource "helm_release" "nginx_ingress" {
  name       = "ingress-nginx"
  namespace  = "ingress-nginx"
  chart      = "ingress-nginx"
  repository = "https://kubernetes.github.io/ingress-nginx"

  create_namespace = true

  # Optionally, you can set values overrides here
  # set {
  #   name  = "controller.replicaCount"
  #   value = "2"
  # }
}
