#!/bin/bash

SERVER="<сервер>"
USER="<пользователь>"

PORT="9999"
HOST="127.0.0.1"

# Проверяем, слушает ли указанный порт
if ! ss -tuln | grep -q "${HOST}:${PORT}"; then
    # Альтернативно можно использовать: lsof -i @${HOST}:${PORT} > /dev/null 2>&1
    echo "Запускаем создание тунеля..."
    ssh -D 9999 -q -C -N -f ${USER}@${SERVER}
else
    echo "Тунель уже создан."
fi