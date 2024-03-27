include ./.env

up:
	docker network ls | grep ${NPM_LAN} > /dev/null || docker network create ${NPM_LAN}
	docker-compose up -d

down:
	docker-compose down -v

# hard
restart: down up

rebuild_:
	docker-compose build --no-cache

rebuild: down rebuild_ up

console:
	docker exec -it ${NAME} /bin/sh

logs:
	docker logs ${NAME} -f

info:
	docker inspect ${NAME}