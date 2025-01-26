terraform {
  backend "azurerm" {
    resource_group_name  = "automation-team-rg"
    storage_account_name = "automationteambackend"
    container_name       = "terraform-backend-ai-rag"
    key                  = "./sample-k8s-app/terraform.tfstate"
    #access_key           = ### SET IN LOCAL ENVIRONEMTNAL VARIABLE ARM_ACCESS_KEY ###
  }
}
