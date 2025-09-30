# Добавление хостового диска в VM

https://www.virtualizationhowto.com/2023/04/proxmox-add-disk-storage-space-nvme-drive/

```
К примеру диск = "sda"
новый лабел = "wd-hdd-500"
папка для монтирования = "wd-hdd-500"
```

Установить:
    apt install parted

Выполнить (но мы уже нашли "sda"):
    lsblk

Пересоздать разде (удалив с него всё что есть):
    parted /dev/sda mklabel gpt

Создаём первичный раздел:
    parted /dev/sda mkpart primary ext4 0% 100%

Форматируем:
    mkfs.ext4 /dev/sda

Задаём лабел:
    mkfs.ext4 -L wd-hdd-500 /dev/sda

Создаём папку для монтирования раздела:
    mkdir /mnt/wd-hdd-500

Автомонтирование:
    nano /etc/fstab

    Добавить в конец файла:
        /dev/sda /mnt/wd-hdd-500 ext4 defaults 0 2

Монтирование раздела:
    mount /mnt/wd-hdd-500

Dataceter -> Storage -> Add -> Direcory:
    id = wd-hdd-500
    Directoty = /mnt/wd-hdd-500
    Content = Все варианты