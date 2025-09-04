include ./.env

up:
	${DOCKER_COMPOSE} up -d

down:
	${DOCKER_COMPOSE} down -v

restart: down up

console:
	docker exec -it redis /bin/bash

logs:
	docker logs redis -f

stats:
	docker stats redis

ip:
	docker inspect redis | grep \"IPAddress\":