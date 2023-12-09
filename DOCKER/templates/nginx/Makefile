include ./.env

up:
	docker network ls | grep ${NPM_LAN} > /dev/null || docker network create ${NPM_LAN}
	docker-compose up -d

down:
	docker-compose down -v

restart: down up