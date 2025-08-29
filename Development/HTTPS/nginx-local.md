# Установка локального Nginx

## Установка Nginx

``` bash
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Установка LetsenCrypt

``` bash
sudo apt install -y letsencrypt python3-certbot-nginx
sudo systemctl status certbot.timer
```

## Получение сертификата через LetsenCrypt



``` bash
sudo certbot certonly --standalone --agree-tos --preferred-challenges http -d blabla.ru
```