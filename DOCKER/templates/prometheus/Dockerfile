# FROM prom/prometheus
FROM ubuntu:latest

ENV TZ=Asia/Vladivostok
RUN apt update && \ 
    apt install tzdata -y && \
    cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt install -y prometheus

# Устанавливаем нужные плагины для сбора данных
#   prometheus-alertmanager         - Менеджер алертов
#   prometheus-node-exporter        - Сбор данных о сервере
#   prometheus-nginx-exporter       - Метрики Nginx
#   prometheus-nginxlog-exporter    -
    
RUN apt install -y prometheus-alertmanager
RUN apt install -y prometheus-node-exporter
RUN apt install -y prometheus-nginx-exporter
# RUN apt install -y prometheus-nginxlog-exporter

