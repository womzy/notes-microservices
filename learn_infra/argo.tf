resource "helm_release" "argocd" {
  name       = "argocd"
  namespace  = "argocd"
  chart      = "argo-cd"
  repository = "https://argoproj.github.io/argo-helm"

  create_namespace = true

  values = [file("argocd-values.yaml")]

  # Optionally, set specific values
  # set {
  #   name  = "server.serviceType"
  #   value = "LoadBalancer"
  # }
}

# output "name" {
#   value = helm_release.argocd.values
# }

resource "kubernetes_manifest" "app_manifest" {
  manifest = {
    "apiVersion" = "argoproj.io/v1alpha1"
    "kind" = "Application"
    "metadata" = {
      "name" = "my-app"
      "namespace" = "argocd"
    }
    "spec" = {
      "destination" = {
        "namespace" = "app"
        "server" = "https://kubernetes.default.svc"
      }
      "project" = "default"
      "source" = {
        "repoURL" = "https://github.com/womzy/notes-microservices.git"
        "targetRevision" = "HEAD"
        "path" = "k8s"
      }
      "syncPolicy" = {
        "automated" = {
          "prune" = true
          "selfHeal" = true
        }
      }
    }
  }
}

