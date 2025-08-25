https://firstvds.ru/technology/kak-sozdat-klyuch-dlya-avtorizacii-po-ssh-i-dobavit-ego-na-server

Локально:

    # Создаём каталог куда положим публичный и приватный ключ
    mkdir -p '/home/<user_local>/.ssh/server1'

    # Генерируем ключи
    ssh-keygen -b 4096 -a 10 -f '/home/<user>/.ssh/server1/id_rsa'
    
    # Отправляем публичный ключ на сервер

    ssh-copy-id -i '/home/<user_local>/.ssh/server1/id_rsa.pub' <user_server>@<ip-сервера>

    или

    cat '/home/<user_local>/.ssh/server1/id_rsa.pub' | ssh <user_server>@<ip-сервера> 'cat >> /home/<user_server>/.ssh/authorized_keys'

Сервер:

    # Если нужно ставим пакеты
    sudo apt install -y openssh-server

    (sudo) /etc/ssh/sshd_config

        AuthorizedKeysFile .ssh/authorized_keys

        PasswordAuthentication no

        UsePAM no

        PermitRootLogin no

    Иногда может потребоваться отключение авторизации по паролю в файлах в каталоге:

        PasswordAuthentication no
        
        /etc/ssh/sshd_config.d

    sudo systemctl restart sshd

Подключение (с приватным ключём):

    chmod 600 ./id_rsa

    ssh -i '/home/<user_local>/.ssh/server1/id_rsa' <user_server>@<ip-сервера>

    или 
    
    Добавить приватный ключ в ssh-агент (что бы не вводить pass-фразу и путь к ключу)
    (Агент помнит ключи только в контексте сессии, если перезагрузиться, то добавлять заново)

        ssh-add '/home/<user_local>/.ssh/server1/id_rsa'

        ssh <user_server>@<ip-сервера>

--------------------------------------------------------------------------------------------------


https://linuxhint.com/generate-ssh-key-ubuntu/

Создание:

    Создать папку для хранения ключей

    Перейти в неё

    ssh-keygen

Копирование на сервер:

    Перейти в папку где лежат нужные ключи

    ssh-copy-id <user name>@<server ip>
    # ssh-copy-id sameza@192.168.1.134
    
    если ошибка, то:

        cat ~/.ssh/<парка с ключём>/<имя ключа>.pub | ssh <user name>@<server ip> "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

        # cat ~/.ssh/dual-server/dual-sameza.pub | ssh sameza@192.168.1.134 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

Удаление пароля из ключа:

    ssh-keygen -p