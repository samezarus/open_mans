# Установка локального Nginx

## Команды

| Команда | Описание |
| - | - |
| Состояние сервиса| systemctl stus nginx |
| Полный перезапуск| systemctl restart nginx |
| Мягкий перезапуск| systemctl reload nginx |
| Проверка конфигурации | nginx -t |

## Установка Nginx

- Каталог с конфигами: /etc/nginx/conf.d/

``` bash
sudo apt update
sudo apt install nginx-full -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Базовая авторизация Nginx

### Установить пакет

``` bash
sudo apt update && sudo apt install apache2-utils
```

### Сгенерировать файл .htpasswd с логином и паролем

``` bash
sudo htpasswd -c /etc/nginx/.htpasswd my_admin
```

### Настройка Nginx (как пример)

`Основной конфиг`

``` commandline
server {
    listen 80;
    server_name your-domain.com;

    location / {
        auth_basic "Требуется первичная авторизация";
        auth_basic_user_file /etc/nginx/.htpasswd;

        proxy_pass http://127.0.0.1:1111;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

`Если есть обработка редиректов в других location и нужно что бы в них не действовала авторизация`
``` commandline
server {
    listen 80;
    server_name your-domain.com;

    location / {
        auth_basic "Требуется первичная авторизация";
        auth_basic_user_file /etc/nginx/.htpasswd;

        proxy_pass http://127.0.0.1:1111;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /api/ {
        auth_basic off;                    # Отключаем базовый auth
        proxy_set_header Authorization ""; # Убираем Authorization из запроса

        proxy_pass https://example.com:1212;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

`Если обработка фронта и есть обработка редиректов в других location и нужно что бы в них не действовала авторизация`
``` commandline
server {
    listen ${PORT} ssl;
    server_name ${HOST_NAME};

    ssl_certificate     /etc/nginx/ssl/${SSL_NAME_PREF}.crt;
    ssl_certificate_key /etc/nginx/ssl/${SSL_NAME_PREF}.key;

    access_log  /var/log/nginx/${HOST}-access.log;
    error_log   /var/log/nginx/${HOST}-error.log;

    root ${DESTINATION};
    index index.html;

    # ----------- Защищённый корень (пример) -----------
    location / {
        auth_basic "Требуется первичная авторизация";
        auth_basic_user_file /etc/nginx/auth/.htpasswd;
        try_files $uri $uri/ /index.html;
    }

    # ----------- ОТКРЫТЫЙ API без Authorization ----------
    location /api/ {
        auth_basic off; # отключаем базовый auth
        proxy_set_header Authorization ""; # Убираем Authorization из запроса

        proxy_pass ${REST_URL}:8001;
        proxy_http_version 1.1;

        # Пробрасываем остальные необходимые заголовки
        proxy_set_header Host $host:${PORT_EXT};
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Connection "";
        proxy_cache_bypass $http_upgrade;

        # При желании скрываем Authorization в ответе
        proxy_hide_header Authorization;
    }

    # (другие location при необходимости)
}
```


## Авторизация по токену

- Конфиг

```
map $http_authorization $auth_ok {
    default          0;
    "Bearer 1234567890" 1;
}

server {
    ...

    location / {
        if ($auth_ok = 0) {
            return 401;
        }

        proxy_pass http://127.0.0.1:11434;
        ...
    }
    
    ...
}
```

- тест (список моделей)

```
  curl https://ollama2.derebass.ru/api/tags \
  -H "Authorization: Bearer 1234567890" \
  -H "Content-Type: application/json" 
```


## LetsenCrypt

### Установка

``` bash
sudo apt install -y letsencrypt python3-certbot-nginx
sudo systemctl status certbot.timer
```

### Получение сертификата домена

``` bash
sudo certbot certonly --standalone --agree-tos --preferred-challenges http -d blabla.ru
```

| Параметр | Описание |
| - | - |
| certonly | Только получение сертификата (без установки на каком-либо web-сервере) |
| standalone | Запуск собственного web-сервер для аутентификации |
| agree-tos  | Принятие ACME соглашения о подписке на сервер |
| preferred-challenges http | Выполнение авторизации с использованием HTTP |


### Добавление поддоменых сертификатов в доменный

``` bash
certbot -d blabla.ru -d api.blabla.ru -d docs.blabla.ru
```

### Расположение сертификатов (симлинки) для Nginx

| Nginx ключ | Расположение |
| - | - |
| ssl_certificate | /etc/letsencrypt/live/blabla.ru/fullchain.pem |
| ssl_certificate_key | /etc/letsencrypt/live/blabla.ru/privkey.pem |

Пример конфига

``` commandline
server {
    listen 443 ssl;

    server_name blabla.ru;
    
    ssl_certificate     /etc/nginx/ssl/live/blabla.ru/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/live/blabla.ru/privkey.pem;

    ...
}
```
