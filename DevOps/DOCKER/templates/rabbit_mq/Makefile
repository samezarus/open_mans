include ./.env

up:
	${DOCKER_COMPOSE} up -d

down:
	${DOCKER_COMPOSE} down -v

restart: down up

console:
	docker exec -it ${RABBIT} /bin/bash

logs:
	docker logs ${RABBIT} -f

stats:
	docker stats ${RABBIT}