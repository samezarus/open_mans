 # https://hub.docker.com/_/mysql/

DB_CNTNR=mysql
DB_NAME=admin
DB_USER=root
DB_PWD=root
RELEVANT_DUMP=~/backups/msql/db.sql

up:
	docker-compose up -d

down:
	docker-compose down -v

start:
	docker start $(DB_CNTNR)

stop:
	docker stop $(DB_CNTNR)

restart:
	docker restart $(DB_CNTNR)

console:
	docker exec -it $(DB_CNTNR) /bin/sh

logs:
	docker logs $(DB_CNTNR) -f

backup:
	docker exec $(DB_CNTNR) /usr/bin/mysqldump -u $(DB_USER) --password=$(DB_PWD) $(DB_NAME) > $(RELEVANT_DUMP)

restore:
	cat $(RELEVANT_DUMP) | docker exec -i $(DB_CNTNR) /usr/bin/mysql -u $(DB_USER) --password=$(DB_PWD) $(DB_NAME)