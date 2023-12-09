git clone https://github.com/apache/superset.git
 
# Переходим в директорию
cd superset
 
# Переключаемся на ветку релиза 1.5.3 (иногда без этого шага не удавалось инсталлировать, поэтому так делаю)
git checkout 1.5.3
 
# Чекаем статус
git status
 
# Теперь нужно поставить версию образа для разветывания с помощью docker-compose.
# Для этого в файле docker-compose-non-dev.yml (в корне проекта) изменяем строчку
# x-superset-image: &amp;superset-image apache/superset:${TAG:-latest-dev}
# или
# x-superset-image: &superset-image apache/superset:${TAG:-latest-dev}
# меняем на
# x-superset-image: &amp;superset-image apache/superset:1.5.3
# или
# x-superset-image: &superset-image apache/superset:1.5.3
 
# Запускаем установку (запустится скачивание образов с hub.docker.com)
только из под рута!!! docker-compose -f docker-compose-non-dev.yml up
 
# ===========================================
# После завершения инсталляции
# Переходим по адресу http://localhost:8088/ 
# и авторизуемся логин/пароль: admin/admin
# ===========================================

########################################################################################

Смена пароля admin:

	docker exec -it superset_app /bin/bash

	superset fab reset-password --username admin --password q0ihygTG0fXVdry4Ec14