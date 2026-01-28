# Portainer

## Установка

### http

``` bash
docker run -d \
-p 9099:9000 \
--name portainer \
--restart=always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
portainer/portainer-ce:latest
```

### nginx + https

- Запуск

``` bash
docker run -d \
-p 127.0.0.1:9443:9443 \
--name portainer \
--restart=always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
portainer/portainer-ce:latest
```

- Конфиг Nginx

- - `${SERVER_NAME}` заменить на DNS-имя сервера, иначе работать не будет
- - `${SSL_PATH}` заменить на путь к папке с сертификатами

``` nginx
server {
    listen 9099 ssl;
    server_name ${SERVER_NAME};

    ssl_certificate       ${SSL_PATH}/cert.crt;
    ssl_certificate_key   ${SSL_PATH}/cert.key;
    
    access_log  /var/log/nginx/portainer-access.log;
    error_log   /var/log/nginx/portainer-error.log;

    location / {
        proxy_pass https://127.0.0.1:9443;

        proxy_ssl_verify off;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;

        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

```

## Сброс настроек

- Сброс, для изменеия параметров запуска (пароль не трогаем)

``` bash
docker stop portainer
docker rm portainer
```

- Сброс пароля (удаление volume)

``` bash
docker stop portainer
docker rm portainer
docker volume rm portainer_data
```