# Graylog

## Man's

```
https://habr.com/ru/companies/otus/articles/703882/
```

## Настройка Graylog

### Очистка БД

- Список индексов: 
``` bash
curl http://127.0.0.1:9200/_cat/indices
```

- Удалить индексы: (где X - номер индекса)
``` bash
curl -XDELETE http://127.0.0.1:9200/graylog_X
```

### Настройка коннекторов

1. http://graylog:port/system/inputs
2. Создать "Beats"


## Связка Graylog с Filebeat

```
https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html
```

### Установка

Учитываем лицемерие НАТы небесной и качаем пакет через МЗТ

```
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.17.3-amd64.deb
sudo dpkg -i filebeat-8.17.3-amd64.deb
```

### Включение модуля logstash

```
filebeat modules enable logstash
```

### Конфигурирование filebeat.yml

1. Открываем /etc/filebeat/filebeat.yml

2. Коментируем все "output-ы"

3. Раскоментируем "output.logstash"

``` yaml
output.elasticsearch:
  hosts: ["http://127.0.0.1:5044"]
```

4. Указать файлы логов

``` yaml
filebeat.inputs:
- type: filestream
  id: id1
  enabled: true
  paths:
    - /home/user/LOGS/*.log
- type: log
  id: id2
  enabled: true
  paths:
    - /home/user/LOGS/frand.log
```


