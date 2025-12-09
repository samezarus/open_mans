include ./.env

up:
	${DOCKER_COMPOSE} up -d
	make set-watermark

down:
	${DOCKER_COMPOSE} down

down_hard:
	${DOCKER_COMPOSE} down -v

restart: down up

rebuild:
	${DOCKER_COMPOSE} build --no-cache

.PHONY: set-watermark
.ONESHELL:
set-watermark:
	sleep 60
	curl -X PUT "http://localhost:9200/_cluster/settings" \
	-H 'Content-Type: application/json' \
	-d '{
	"persistent": {
	"cluster.routing.allocation.disk.watermark.low": "97%",
	"cluster.routing.allocation.disk.watermark.high": "98%",
	"cluster.routing.allocation.disk.watermark.flood_stage": "99%"
	}
	}'