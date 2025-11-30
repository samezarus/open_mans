# VPN через SSH

## Установка

``` bash
sudo apt update && sudo apt install -y sshuttle
```

## Использование

``` bash
sudo sshuttle --dns -r user@ssh-host 192.168.2.0/24
```