# По мотивам:
https://github.com/wmnnd/nginx-certbot

https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

# Шаги:

## Скопировать заготовку переменных
cp .env.example .env

## Задать переменные в .env
DOMAIN=<ваш домен>
EMAIL=<ваша реальная почта>

## Сделать скрипт исполняемым
chmod +x init-letsencrypt.sh

## Выполнить скрипт
./init-letsencrypt.sh

# Траблшутинг:

1. Убедиться что на сервере разрешены 80 и 443 порт