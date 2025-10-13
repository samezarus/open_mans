# Настройка и запуск Sentry

## Инициализация

1. Сгенирировать ключ

``` bash
make key
```

2. Полученый ключ поместить в .env-файл

```
...
SENTRY_SECRET_KEY='<key>'
...
```

3. Инициализация и Sentry (только при первом запуске проекта)

``` bash
make init
```

4. В процессе инициализации нужно создать логин и пароль админа

```
... 
Would you like to create a user account now? [Y/n]: 
...
```

5. Web-интерфейс Sentry будет доступен по адресу `https://<ip/dns-машины>:9000`

## Использование в связке с Nginx

1. Должна быть пройдена инициализация

2. В .env файле заменить значение переменной `SENTRY_WEB_HOST` на `127.0.0.1`

```
...
SENTRY_WEB_HOST="127.0.0.1"
...
```

3. Перезапустить проект

``` bash
make restart
```

4. Конфиг Nginx

```
...
server {
    listen 9001 ssl http2;
    #listen 9001;
    #server_name sentry.example.com;

    ssl_certificate     /home/prod/.self_ssl/cert.crt;
    ssl_certificate_key /home/prod/.self_ssl/cert.key;

    location / {
        proxy_pass http://127.0.0.1:9000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
...
```

5. Web-интерфейс Sentry будет доступен по адресу `https://<ip/dns-сервера>:9001`