# Rabbit MQ

## Запуск 

`Задать нужные переменные в .env файле`

### http

``` bash
make up
```

### https

`Nginx должен быть установлен "sudo apt install nginx-full -y"`
`В "/etc/nginx/nginx.conf" добавить строку "include /etc/nginx/streams-enabled/*.conf;" выше секции "http {...}"`


- Переопределить переменный в .env-файле !
- - `RABBIT_PORT` сделать отличным от 5672 (к примеру 5673)
- - `RABBIT_PORT_WEB` сделать отличным от 15672 (к примеру 15673)

- Задать переменные для Nginx
- - `${SSL_PATH}` заменить на путь к папке с сертификатами

#### amqp конфиг Nginx (/etc/nginx/streams-enabled/rabbitmq_stream.conf)

``` stream
stream {
    # TLS‑терминация для AMQP
    upstream rabbit_amqp_plain {
        server 127.0.0.1:5673;
    }

    server {
        listen 5672 ssl;
        ssl_certificate       ${SSL_PATH}/cert.crt;
        ssl_certificate_key   ${SSL_PATH}/cert.key;

        proxy_pass rabbit_amqp_plain;
        proxy_timeout 10s;
        proxy_connect_timeout 1s;
    }
```

#### web/ui конфиг Nginx (/etc/nginx/sites-availabl/default)

``` nginx
server {
    listen 15672 ssl;
    server_name _;

    ssl_certificate       ${SSL_PATH}`/cert.crt;
    ssl_certificate_key   ${SSL_PATH}`/cert.key;
    
    access_log  /var/log/nginx/rabbitmq-access.log;
    error_log   /var/log/nginx/rabbitma-error.log;

    location / {
        proxy_pass          http://127.0.0.1:15673;
        proxy_set_header    Host $host;
        proxy_set_header    X-Real-IP $remote_addr;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto $scheme;

        # WebSocket‑поддержка (если используете STOMP/Web‑STOMP)
        proxy_http_version  1.1;
        proxy_set_header    Upgrade $http_upgrade;
        proxy_set_header    Connection "upgrade";
    }
}

```