# QEMU/KVM

## Установка

- qemu-kvm – сам гипервизор.
- libvirt – слой управления (можно использовать virsh, virt-manager и т.п.).
- bridge-utils – если планируете создавать сетевые мосты.
- virt-manager – графический менеджер виртуальных машин.

``` bash
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager -y
```