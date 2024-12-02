up:
	docker compose up -d

down:
	docker compose down -v

restart: down up

rebuild:
	docker compose build --no-cache

logs:
	docker logs -f prometheus

console:
	docker exec -it prometheus /bin/sh