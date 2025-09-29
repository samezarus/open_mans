include ./.env

up:
	docker-compose up -d

down:
	docker-compose down -v

start:
	docker start ${AFS}

stop:
	docker stop ${AFS}

restart:
	docker restart ${AFS}

console:
	docker exec -it ${AFS} /bin/sh

logs:
	docker logs ${AFS} -f
