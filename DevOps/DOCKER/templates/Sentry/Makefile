include ./.env

# Генерация ключа
key:
	docker run --rm sentry config generate-secret-key

# Контейнер для запуска миграция БД Sentry
_upgrade:
	docker run -it --rm \
    -e SENTRY_SECRET_KEY='${SENTRY_SECRET_KEY}' \
    -e SENTRY_POSTGRES_HOST='${DB}' \
	-e SENTRY_POSTGRES_PORT='${DB_PORT}' \
    -e SENTRY_DB_NAME='${DB_NAME}' \
    -e SENTRY_DB_USER='${DB_USER}' \
    -e SENTRY_DB_PASSWORD='${DB_PASSWORD}' \
    -e SENTRY_REDIS_HOST='${REDIS}' \
	-e SENTRY_REDIS_PORT='${REDIS_PORT}' \
    --network 'sentry_default' \
    sentry upgrade

# Инициализация Sentry
# Запускать только после генирации и записи ключа в .env-файл
init:
# 	docker network create ${LAN}
	${DOCKER_COMPOSE} --profile init up -d
	make _upgrade
	make down
	make up

# Запуск всего проекта Sentry
up:
	${DOCKER_COMPOSE} --profile prod up -d

# Остановка всего проекта Sentry
down:
	${DOCKER_COMPOSE} --profile init --profile prod down

# Перезапуск всего проекта Sentry
restart: down up

# !!! Остановка всего проекта Sentry с очисткой всех volume's !!!
down_hard:
	${DOCKER_COMPOSE} --profile init --profile prod down -v


