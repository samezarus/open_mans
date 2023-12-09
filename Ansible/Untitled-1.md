https://www.youtube.com/watch?v=ctUP2nrkNCY

========================================================================================================================

ping (встроенный):
    ansible all -m ping

Выполнение команд:
    ansible all -m shell -a "uptime"
    или
    ansible all -m command -a "uptime"

Копирование с сервера ansible на хосты:
    ansible all -m copy -a "src=/home/<user>/test.txt dest=/home/ mode=777" -b

Запуск playbook-а:
    ansible-playbook <путь к файлу playbook-а>

Копирование с удалённой машины на сервер ansible:
    На удалённом хосте у пользователя sudo не должно просить пароль!

    playbook (test.yml):
        - name: Get backups from unilab.su
          hosts: unilab.su
          become: yes

          tasks:

          - name: Get db backup
            fetch:
              src: "/home/prod/PROD_PROJECTS_FILES/unilabsu_django/logs/old_reg.log"
              dest: "./old_reg.log"
              flat: yes
    
    Страт playbook-а:
        ansible-playbook ./test.yml

========================================================================================================================

Установка: 

    https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-22-04

    sudo apt-add-repository ppa:ansible/ansible

    sudo apt update

    sudo apt install ansible sshpass -y

========================================================================================================================

Конфигурация:

    Перейти в домашнюю директорию:
        cd /home/<user>/

    Если нет, то создать директорию .ansible:
        mkdir .ansible

    Перейти в директорию .ansible:
        cd /home/<user>/.ansible/

    Создать, если несоздан файл ansible.cfg:
        > ansible.cfg

    Добавить настройки в ansible.cfg:
        [defaults]
        inventory = /home/<user>/.ansimble/inventory  # расположение файла inventory
        host_key_cheking = False  # не требовать проверки сертификата от хоста
        deprecation_warnings = False  # Отключить уведомления о "старье"

    Проверить файл конфигурации ansible.cfg:
        ansimble --version

    Создать файл inventory:
        > inventory

    В файл inventory добавить хосты:
        [servers]
        server1 ansible_host=203.0.113.111 ansible_user='<ssh user>' ansible_password='<ssh password>'
        server2 ansible_host=203.0.113.112 ansible_user='<ssh user>' ansible_ssh_private_key_file='<путь к файлу ssh-ключа>'
        [all:vars]
        ansible_ssh_common_args='-o StrictHostKeyChecking=no'  # не требовать проверки сертификата от хоста

    Проверка фала inventory:
        ansible-inventory --list -y

========================================================================================================================