up:
	docker-compose up -d

down:
	docker-compose down -v

restart: down up

rebuild:
	docker-compose build --no-cache
	docker image prune -f

console:
	docker exec -it ${DJANGO_NAME} /bin/bash
	
logs:
	docker logs ${DJANGO_NAME} -f