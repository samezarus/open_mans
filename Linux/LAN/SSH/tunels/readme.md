# Local2Remote

## Прокидываем порт с локальной машины в удалённую


### В фоновом режиме

``` bash
ssh -L 8080:localhost:80 -N -f <user>@<remote_host>
```

# Remote2Local


# Proxy ()

``` bash
ssh -D <port> -q -C -N -f <user>@<host>
```

Открыть к примеру броузер, настройки proxy 

SOCKS v5:

- SOCKS Host = <host>
- Port = <port>