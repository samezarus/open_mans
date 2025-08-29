# Установка локального Nginx и LetsenCrypt

## Nginx

### Установка

``` bash
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

### Базовая авторизация

1. Установить пакет:

``` bash
sudo apt update && sudo apt install apache2-utils
```

2. Сгенерировать файл .htpasswd с логином и паролем:

``` bash
sudo htpasswd -c /etc/nginx/.htpasswd admin
```

Настройка Nginx (как пример):

```
server {
    listen 8080;
    server_name blabla.ru;

    location / {
        auth_basic "bla bla bla";
        auth_basic_user_file /etc/nginx/.htpasswd;

        proxy_pass http://ollama:11434;
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

### Получение сертификата

``` bash
sudo certbot certonly --standalone --agree-tos --preferred-challenges http -d blabla.ru
```

### Добавление поддоменов к ранее выпущенному сертификату

``` bash
sudo certbot --nginx -d blabla.ru -d api.blabla.ru
```

### Расположение сертификатов

- /etc/letsencrypt/live/blabla.ru/fullchain.pem (ssl_certificate)
- /etc/letsencrypt/live/blabla.ru/privkey.pem (ssl_certificate_key)