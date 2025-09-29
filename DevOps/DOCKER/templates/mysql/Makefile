# https://hub.docker.com/_/mysql/

include ./.env

DUMP=${DB_BACKUP_FOLDER}/${DB_BACKUP_PREFIX}
DUMP_TS=$(DUMP)_`date +%Y-%m-%d"_"%H_%M_%S`

up:
	docker-compose up -d

down:
	docker-compose down -v

start:
	docker start ${DB}

stop:
	docker stop ${DB}

restart:
	docker restart ${DB}

# hard restart
restart_h: down up

console:
	docker exec -it ${DB} /bin/sh

logs:
	docker logs ${DB} -f

sleep:
	sleep 30s

# backup: $(DUMP).sql
backup:
	docker exec ${DB} /usr/bin/mysqldump -u ${DB_ROOT} --password=${DB_PASSWORD_ROOT} ${DB_NAME} > $(DUMP).sql

# backup: $(DUMP)_<TimeStamp>.sql
backup_ts:
	docker exec ${DB} /usr/bin/mysqldump -u ${DB_ROOT} --password=${DB_PASSWORD_ROOT} ${DB_NAME} > $(DUMP_TS).sql

# restore
restore:
	cat $(DUMP).sql | docker exec -i ${DB} /usr/bin/mysql -u ${DB_ROOT} --password=${DB_PASSWORD_ROOT} ${DB_NAME}

# hard restore
restore_h: restart_h sleep restore

# soft restore (with prebackup old base)
restore_s: backup_ts restart_h sleep restore

# backup: $(DUMP).gz
backup_arc:
	docker exec ${DB} /usr/bin/mysqldump -u ${DB_ROOT} --password=${DB_PASSWORD_ROOT} ${DB_NAME} | gzip > $(DUMP).gz

# backup: $(DUMP)_<TimeStamp>.gz
backup_arc_ts:
	docker exec ${DB} /usr/bin/mysqldump -u ${DB_ROOT} --password=${DB_PASSWORD_ROOT} ${DB_NAME} | gzip > $(DUMP_TS).gz

# restore from arc
restore_arc:
	gunzip < $(DUMP).gz | docker exec -i ${DB} /usr/bin/mysql -u ${DB_ROOT} --password=${DB_PASSWORD_ROOT} ${DB_NAME}

# hard restore from arc
restore_arc_h: restart_h sleep restore_arc

# soft restore from arc (with prebackup old base in arc)
restore_arc_s: backup_arc_ts restart_h sleep restore_arc