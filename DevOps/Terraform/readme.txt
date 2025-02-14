https://developer.hashicorp.com/terraform/cli

Install:

    Вариант 1:

        sudo snap install terraform --classic

Use:

    Создать папку, создать в ней любой файл с расширением ".tf"

        main.tf

    Для старта инициализации, нужно хотя бы определить провайдера:

        TimeWeb:

            terraform {
                required_providers {
                    twc = {
                    source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
                    }
                }
                required_version = ">= 1.4.4"
            }

        Yandex:

            terraform {
                required_providers {
                    yandex = {
                    source = "yandex-cloud/yandex"
                    }
                }
                required_version = ">= 0.13"
            }

    Инициализация конфы:

        terraform init

        PS:
            Если в конфе есть ресурс "cloudinit_config" или ресурсы которые образаются 
            к "registry.terraform.io/...", то следует включить VPN.

                Error: Invalid provider registry host
                The host "registry.terraform.io" given in provider source 
                address "registry.terraform.io/hashicorp/cloudinit" does not offer a
                Terraform provider registry.

    Вывод плана конфы:

        terraform plan

    Валидация конфы:

        terraform validate

    Пушь конфы на сервер:

        terraform apply -auto-approve

    Остановка и удаление конфы с сервера:

        terraform destroy -auto-approve

