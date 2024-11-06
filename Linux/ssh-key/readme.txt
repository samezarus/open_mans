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