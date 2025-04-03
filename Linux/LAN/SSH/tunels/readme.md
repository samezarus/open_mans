# Local2Remote

## Прокидываем порт с локальной машины в удалённую


### В фоновом режиме

```
ssh -L 8080:localhost:80 -N -f user@remote_host
```

# Remote2Local