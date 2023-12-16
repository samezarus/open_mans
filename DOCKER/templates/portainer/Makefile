include ./.env

up:
	docker-compose up -d

down:
	docker-compose down -v

restart: down up

cli:
	docker exec -it ${PORTAINER} /bin/bash

logs:
	docker logs -f ${PORTAINER}

env:
	docker exec -it ${PORTAINER} printenv