# Установка локального Nginx

## Установка Nginx

- Каталог с конфигами: /etc/nginx/conf.d/

``` bash
sudo apt update
sudo apt install nginx -y
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
sudo htpasswd -c /etc/nginx/.htpasswd admin
```

### Настройка Nginx (как пример)

``` commandline
server {
    listen 80;
    server_name your-domain.com;

    location / {
        auth_basic "bla bla bla";
        auth_basic_user_file /etc/nginx/.htpasswd;

        proxy_pass http://127.0.0.1:11434;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
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
certbot --nginx -d blabla.ru -d api.blabla.ru -d docs.blabla.ru
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
