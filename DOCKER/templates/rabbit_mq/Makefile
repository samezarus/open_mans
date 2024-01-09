include ./.env

up:
	docker-compose up -d

down:
	docker-compose down -v

restart: down up

console:
	docker exec -it ${RABBIT} /bin/bash

logs:
	docker logs ${RABBIT} -f

django_stats:
	docker stats ${RABBIT}