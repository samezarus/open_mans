1. Стратуем мини compose для поднятия postgre и redis:
        
    docker compose up -d -f ./docker-compose_init.yml

2. Запускаем инициализирующий контейнер для миграций в postgre и задания админа:

    docker run -it --rm \
    -e SENTRY_SECRET_KEY='<env.SENTRY_SECRET_KEY>' \
    -e SENTRY_POSTGRES_HOST='<env.DB>' \
    -e SENTRY_POSTGRES_PORT=<env.DB_PORT> \
    -e SENTRY_DB_NAME='<env.DB_NAME>' \
    -e SENTRY_DB_USER='<env.DB_USER>' \
    -e SENTRY_DB_PASSWORD='<env.DB_PASSWORD>'\
    -e SENTRY_REDIS_HOST='<env.REDIS>' \
    -e SENTRY_REDIS_PORT=<env.REDIS_PORT> \
    --network '<env.NETWORK>' \
    sentry upgrade

3. Останавливаем мини compose:

    docker compose down

4. Правим конфиги, которые sentry "выплюнула" в ./sentry/sentry:

    config.yml:

        system.secret-key = <env.SENTRY_SECRET_KEY>

        redis.clusters ... host = <env.REDIS>

    sentry.conf.py:

        DATABASES = env.DB, env.DB_PORT, env.DB_NAME, env.DB_USER, env.DB_PASSWORD

        BROKER_URL = env.REDIS

        SENTRY_WEB_HOST = <env.SENTRY>

        SENTRY_WEB_PORT = <env.SENTRY_PORT>

5. Стартуем основной compose:

    docker compose up -d    