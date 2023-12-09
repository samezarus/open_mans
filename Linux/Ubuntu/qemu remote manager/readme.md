Создать RSA-ключи (ssh-key)

Закинуть их на серверу

Установить пакеты на сервере:
    https://help.ubuntu.com/community/KVM/VirtManager
    https://fabianlee.org/2019/02/16/kvm-virt-manager-to-connect-to-a-remote-console-using-qemussh/

    sudo apt-get install virt-manager ssh-askpass-gnome --no-install-recommends

Добавление коннекта на машине с которй будем подсоединяться к серверу (Ubuntu GUI):

    virt-manager -c 'qemu+ssh://<user>@<server>:<ssh port>/system?keyfile=<путь к папке с закрытым ключём>/<имя-файла закрытого ключа>'

    # virt-manager -c 'qemu+ssh://sameza@192.168.1.134:22/system?keyfile=/home/sameza/.ssh/dual-server/dual-sameza'