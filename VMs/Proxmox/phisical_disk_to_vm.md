# Маппинг физического диска в VM


Переменные для примера:

| Переменная | Значение |
|  |  |
| vm-id | 104 |
| index | 1 |
| ident | ata-KINGSTON_SV300S37A480G_50026B7673014EE9 |
| vm-disk-dev | /dev/sdb |
| vm-disk-label | sg-hdd-250 |
| vm-disk-mount-folder | ${vm-disk-label} |

## Кстановить зависимости
    
``` bash
sudo apt install -y lshw parted lsblk
```
   
## Шаги (Proxmox host)

- Выбор нужного диска по id (sata)

``` bash
ls -l /dev/disk/by-id/ | grep ata-
```

```
Пример:

lrwxrwxrwx 1 root root  9 Sep 25 13:25 ata-KINGSTON_SV300S37A480G_50026B7673014EE9 -> ../../sdb
lrwxrwxrwx 1 root root  9 Sep 20 08:59 ata-WDC_WD5003ABYX-01WERA2_WD-WMAYP6790825 -> ../../sda
```

- Подключение диска к VM

``` bash
qm set ${vm-id} -scsi${index} /dev/disk/by-id/${ident}
```

```
Пример:

qm set 104 -scsi1 /dev/disk/by-id/ata-KINGSTON_SV300S37A480G_50026B7673014EE9
```

## Шаги (Внутри VM)

- Поиск точки монтирования

``` bash
ls -l /dev/disk/by-id/ | grep drive-scsi | grep /sd
```

```
Пример:
        
lrwxrwxrwx 1 root root  9 Sep 28 13:26 scsi-0QEMU_QEMU_HARDDISK_drive-scsi1 -> ../../sdb

vm-disk-dev = /dev/sdb
```

- Форматирование (если надо)

    Пересоздать разде (удалив с него всё что есть):
        parted ${vm-disk-dev} mklabel gpt

    Создаём первичный раздел:
        parted ${vm-disk-dev} mkpart primary ext4 0% 100%

    Форматируем:
        mkfs.ext4 ${vm-disk-dev}

    Пример:
        parted /dev/sdb mklabel gpt

        parted /dev/sdb mkpart primary ext4 0% 100%

        mkfs.ext4 /dev/sdb

- Монтирование

    Задаём лабел:
        mkfs.ext4 -L ${vm-disk-label} ${vm-disk-dev}

    Создаём папку для монтирования раздела:
        mkdir /mnt/${vm-disk-mount-folder}

    Автомонтирование:
        nano /etc/fstab

        Добавить в конец файла:
            ${vm-disk-dev} /mnt/${vm-disk-mount-folder} ext4 defaults 0 2

    Монтирование раздела:
        mount ${vm-disk-dev} /mnt/${vm-disk-mount-folder}

    Перезагрузить систему или "systemctl daemon-reload"

    При удачном монтировании в утилите lsblk можно посмотреть смонтировался ли диск:
        В колонке MOUNTPOINTS будет указан каталог монтирования



    Пример:
        mkfs.ext4 -L sg-hdd-250 /dev/sdb
        mkdir /mnt/sg-hdd-250

        nano /etc/fstab
            /dev/sdb /mnt/sg-hdd-250 ext4 defaults 0 2    

        mount /dev/sdb /mnt/sg-hdd-250

        reboot

        lsblk
            NAME                 MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
            sda                    8:0    0    32G  0 disk 
            ├─sda1                 8:1    0     1M  0 part 
            ├─sda2                 8:2    0     2G  0 part /boot
            └─sda3                 8:3    0    30G  0 part 
                └─ubuntu--vg-lv--0 253:0    0    29G  0 lvm  /
            sdb                    8:16   0 232.9G  0 disk /mnt/sg-hdd-250
            sr0                   11:0    1   1.4G  0 rom  


