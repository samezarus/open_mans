include ./.env

up:
	docker-compose up -d

down:
	docker-compose down -v

restart: down up

rebuild_php:
	docker-compose down -v
	docker-compose build --no-cache ${PHP}
	docker-compose up -d

console:
	docker exec -it ${PHP} /bin/sh

