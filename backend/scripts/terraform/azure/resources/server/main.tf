terraform {
  required_version = ">= 1.0.0"

  required_providers {
    azurem = {
      source = "hashicorp/azurem"
      version = "~> 3.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.14.0"
    }
  }
}

provider "azurerm" {
  features {}
}