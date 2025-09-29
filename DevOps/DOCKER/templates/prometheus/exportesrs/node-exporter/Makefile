up:
	docker compose up -d

down:
	docker compose down -v

restart: down up

rebuild:
	docker compose build --no-cache

logs:
	docker logs -f node-exporter

console:
	docker exec -it node-exporter /bin/sh