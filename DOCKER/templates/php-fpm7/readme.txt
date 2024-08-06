Смена настроек

    /.default.conf

        fastcgi_pass <php container>:9000;

    ./src/back/db/config_db.php
        
        'host' => '',
        'port' => '',
        'dbname' => '',
        'user' => ''
        'password' => ''

    ./docker-compose.yml

        nginx_<prefix>:
            container_name: nginx_<prefix>
            image: nginx:latest
            ports:
                - '<port>:80'
            volumes:
                - ./src:/var/www/html
                - ./default.conf:/etc/nginx/conf.d/default.conf
            links:
                - <php_container>

        <php_container>:
            container_name: <php_container>
            build: 
                context: ./
                dockerfile: ./php_parent.Dockerfile
            volumes:
                - ./src:/var/www/html

    ./Makefile

        PHP_CNTR=<from docker-compose.yml>
        NGINX_CNTR=<from docker-compose.yml>

    