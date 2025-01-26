resource "azurerm_resource_group" "rg" {
  name     = "my-aks-rg"
  location = "North Europe"
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "womzy-aks-cluster"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "womzyakscluster"   # DNS prefix for the Kubernetes cluster e.g https://womzyakscluster.northeurope.azmk8s.io

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}

# output "kube_config" {
#   value     = azurerm_kubernetes_cluster.aks.kube_config_raw
#   sensitive = true
# }


# output "client_certificate" {
#   value     = azurerm_kubernetes_cluster.aks.kube_config[0].client_certificate
#   sensitive = true
# }


