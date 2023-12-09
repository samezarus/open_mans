include ./.env

BACKUPS_DIR=~/backups/${DB_HOST}/

DUMP=$(BACKUPS_DIR)`date +%Y-%m-%d"_"%H_%M_%S`.sql
RELEVANT_DUMP=$(BACKUPS_DIR)db.sql

DUMP_ARC=$(BACKUPS_DIR)`date +%Y-%m-%d"_"%H_%M_%S`.gz
RELEVANT_DUMP_ARC=$(BACKUPS_DIR)db.gz

ERROR_DUMP_FILE_DONT_EXISTS="Отсутствует файл-дамп "$(RELEVANT_DUMP)" для восстановления БД в контейнере "${DB_HOST}

up:
	docker-compose up -d

down:
	docker-compose down -v

# Бэкапирование БД
backup:
	@mkdir $(BACKUPS_DIR) -p # Создание директории для бэкапов, если её вдруг нет
	@docker exec -t ${DB_HOST} pg_dumpall -c -U ${DB_USER} > $(RELEVANT_DUMP) # Создание дампа текущего состояния БД
	@cp $(RELEVANT_DUMP) $(DUMP) # Пометка датой и временем дампа текущего состояния БД

# Бэкапирование БД с архивацией
backup_arc:
	@mkdir $(BACKUPS_DIR) -p # Создание директории для бэкапов, если её вдруг нет
	@docker exec -t ${DB_HOST} pg_dumpall -c -U ${DB_USER} | gzip > $(RELEVANT_DUMP_ARC) # Создание дампа текущего состояния БД (архивированиние)
	@cp $(RELEVANT_DUMP_ARC) $(DUMP_ARC) # Пометка датой и временем дампа текущего состояния БД

# Восстановление БД
restore:
	@[ -f $(RELEVANT_DUMP) ] \
	&& (sleep 5; cat $(RELEVANT_DUMP) | docker exec -i ${DB_HOST} psql -U ${DB_USER} -d ${DB_NAME}) \
	|| (echo "restore: "$(ERROR_DUMP_FILE_DONT_EXISTS); exit 1)

# Восстановление БД из файла-архива
restore_arc:
	@[ -f $(RELEVANT_DUMP_ARC) ] \
	&& (sleep 5; gunzip < $(RELEVANT_DUMP_ARC) | docker exec -i ${DB_HOST} psql -U ${DB_USER} -d ${DB_NAME}) \
	|| (echo "restore: "$(ERROR_DUMP_FILE_DONT_EXISTS); exit 1)
