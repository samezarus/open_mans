https://github.com/nginxinc/nginx-prometheus-exporter

https://hub.docker.com/r/nginx/nginx-prometheus-exporter


В наблюдаемом nginx должен быть открыт и слушаться порт 8080

    nginx.docker-compose.yaml

        ...
        ports:
        - 127.0.0.1:8080:8080
        ...

В наблюдаемом nginx должно быть правило прослушивания порта 8080

    ./nginx-exporter.conf.template

        server {
            listen 8080;

            access_log /var/log/nginx/nginx-exporter-access.log;
            error_log  /var/log/nginx/nginx-exporter-error.log;

            server_name _;

            location /stub_status {
                stub_status;
            }
        }