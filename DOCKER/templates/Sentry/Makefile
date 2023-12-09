include ./.env

up:
	docker-compose up -d

down:
	docker-compose down -v

restart: down up

# Генерация ключа
key:
	docker run --rm sentry config generate-secret-key

# Инициализация, один раз после установки
init:
	docker run -it --rm \
	-e TZ=${TZ} \
	-e SENTRY_SECRET_KEY=${SENTRY_SECRET_KEY} \
	-e SENTRY_POSTGRES_HOST=${DB} \
	-e SENTRY_POSTGRES_PORT=${DB_PORT} \
	-e SENTRY_DB_NAME=${DB_NAME} \
	-e SENTRY_DB_USER=${DB_USER} \
	-e SENTRY_DB_PASSWORD=${DB_PASSWORD} \
	-e SENTRY_REDIS_HOST=${REDIS} \
	--link ${DB}:${DB} \
	--link ${REDIS}:${REDIS} \
	--network ${NPM_LAN} \
	sentry upgrade