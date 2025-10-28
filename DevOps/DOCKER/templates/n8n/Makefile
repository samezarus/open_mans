include ./.env

# Запуск проекта
up:
	${DOCKER_COMPOSE} up -d

# Остановка проекта
down:
	${DOCKER_COMPOSE} down

# Перезапуск проекта
restart: down up

# !!! Остановка проекта с очисткой всех volume's !!!
down_hard:
	${DOCKER_COMPOSE} down -v