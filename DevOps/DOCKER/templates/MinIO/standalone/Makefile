include ./.env

up:
	${DOCKER_COMPOSE} up -d
	
down:
	${DOCKER_COMPOSE} down

restart: down up

rebuild:
	${DOCKER_COMPOSE} build --no-cache
	docker image prune -f

console:
	docker exec -it ${MINIO} /bin/bash

logs:
	docker logs ${MINIO} -f