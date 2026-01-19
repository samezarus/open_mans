# VPN через SSH

## Установка

``` bash
sudo apt update && sudo apt install -y sshuttle
```

## Тест

``` bash
sudo iptables -L >/dev/null 2>&1 && echo "iptables OK" || echo "sudo iptables НЕ работает"
```

## Использование

- Без DNS (интернет остаётся локальным)

``` bash
sudo sshuttle -v -r user@ssh-host 192.168.2.0/24
```

- С DNS (интернет из удалённой сети)

``` bash
sudo sshuttle -v --dns -r user@ssh-host 192.168.2.0/24
```