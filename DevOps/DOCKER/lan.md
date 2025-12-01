# Шпора для работы с сетью

## Просмотреть сети

``` bash
sudo iptables -L -n -v | grep -i docker
```

## Правил NAT‑таблицы, отвечающих за публикацию портов

``` bash
sudo iptables -t nat -L DOCKER -n -v
```