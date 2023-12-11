include ./.env

up:
	docker-compose up -d

down:
	docker-compose down -v

restart: down up

# services

# 	Promtail
logs-p:
	docker logs ${P} -f

cli-p:
	docker exec -it ${P} /bin/bash

restart-p:
	docker restart ${P}

# 	Loki
logs-l:
	docker logs ${L} -f

cli-l:
	docker exec -it ${L} /bin/bash

restart-l:
	docker restart ${L}

# 	Grafana
logs-g:
	docker logs ${G} -f

cli-g:
	docker exec -it ${G} /bin/bash

restart-g:
	docker restart ${G}
