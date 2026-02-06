# Установка:

``` bash
sudo apt install -y python3-pip python3.12-venv
pip install --break-system-packages virtualenv
```

# Создание и активация:

``` bash
python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip
```

``` bash
python -m venv .venv && source .venv/bin/activate && pip install --upgrade pip
```

# Создание с версией python:

``` bash
virtualenv -p /usr/bin/python3.11 .venv
```

# Активация

``` bash
source .venv/bin/activate
```


# Деактивация:

``` bash
deactivate
```
    
# Установка зависимостей:

``` bash
pip install -r ./requirements.txt
```