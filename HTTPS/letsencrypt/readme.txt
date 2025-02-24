https://serverspace.ru/support/help/lets-encrypt-ubuntu-20-04/?utm_source=google.com&utm_medium=organic&utm_campaign=google.com&utm_referrer=google.com

----------------------------------------------------------------------------------------

Открываем порты (если нужно):

    sudo ufw allow 80
    sudo ufw allow 443

Установка пакета:

    sudo apt install -y letsencrypt python3-certbot-nginx

Проверка, что таймер обновления сертов работает:

    sudo systemctl status certbot.timer

Получение серта:

    sudo certbot certonly --standalone --agree-tos --preferred-challenges http -d blabla.ru

        certonly                  - только получение сертификата (без установки на каком-либо web-сервере)
        standalone                - запуск собственного web-сервер для аутентификации
        agree-tos                 - принятие ACME соглашения о подписке на сервер
        preferred-challenges http - выполнение авторизации с использованием HTTP

    Если нужен серт на поддомен:

        certbot --nginx -d blabla.ru -d api.blabla.ru

Использование в Nginx (хост):

    ssl_certificate     /etc/letsencrypt/live/blabla.ru/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/blabla.ru/privkey.pem;

Использование в Nginx (docker):

    Вся соль в том, что 
        /etc/letsencrypt/live/blabla.ru/fullchain.pem;
        /etc/letsencrypt/live/blabla.ru/privkey.pem;

    это симлинки на
        fullchain.pem -> ../../archive/blabla.ru/fullchain1.pem
        privkey.pem -> ../../archive/blabla.ru/privkey1.pem

    И по этому в контейнер нужно мапить папку /etc/letsencrypt/, что бы симлинка
    могла лостучаться до /etc/letsencrypt/archive/blabla.ru/

     
    В докер стоит прокидывать вольюм 

        К примеру:
            volumes:
              ...
              - /etc/letsencrypt:/etc/nginx/ssl
              ...

        Конфиг сайта:

            server {
                listen 443 ssl;
                server_name blabla.ru;
                ssl_certificate     /etc/nginx/ssl/live/blabla.ru/fullchain.pem;
                ssl_certificate_key /etc/nginx/ssl/live/blabla.ru/privkey.pem;
            }
    
