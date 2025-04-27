# V1

## Ссылка на статью
- https://raspberrypi.ru/forum/topic/4432/%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D0%B5%D0%BC-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D1%83-%D0%BA-raspberry-pi-5

## Переключение pci-e в GEN 3


 - dtparam=pciex1_gen=3 -> /boot/firmware/config.txt

или через

``` bash
sudo raspi-config
```

## Проверка что карта видна в системе

``` bash
lspci
```

## Подготовка к пересборке ядра

- https://www.raspberrypi.com/documentation/computers/linux_kernel.html#building

``` bash
sudo apt install git
```

``` bash
git clone --depth=1 https://github.com/raspberrypi/linux
```

``` bash
sudo apt install bc bison flex libssl-dev make
```

## Пересборка ядра (pi5 64-bit)

``` bash
cd linux
KERNEL=kernel_2712
make bcm2712_defconfig
```

``` bash
make -j6 Image.gz modules dtbs
```

``` bash
sudo make -j6 modules_install
```

``` bash
sudo cp /boot/firmware/$KERNEL.img /boot/firmware/$KERNEL-backup.img
sudo cp arch/arm64/boot/Image.gz /boot/firmware/$KERNEL.img
sudo cp arch/arm64/boot/dts/broadcom/*.dtb /boot/firmware/
sudo cp arch/arm64/boot/dts/overlays/*.dtb* /boot/firmware/overlays/
sudo cp arch/arm64/boot/dts/overlays/README /boot/firmware/overlays/
```

``` bash
sudo reboot
```

``` bash
sudo apt install bc bison flex libssl-dev make libc6-dev libncurses5-dev
```

``` bash
sudo apt install crossbuild-essential-arm64
```

``` bash
cd linux
KERNEL=kernel_2712
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- bcm2712_defconfig
```

``` bash
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- Image modules dtbs
```


# V2
- https://alican-kiraz1.medium.com/run-llm-on-pi5-connecting-an-nvidia-gpu-to-raspberry-pi-5-via-pcie-x4-a6d52c3efd2a

``` bash
wget https://github.com/hertg/egpu-switcher/releases/download/0.19.0/egpu-switcher-arm64
```

``` bash
sudo cp egpu-switcher-arm64 /opt/egpu-switcher
sudo chmod 755 /opt/egpu-switcher
sudo ln -s /opt/egpu-switcher /usr/bin/egpu-switcher
sudo egpu-switcher enable
```

``` bash
sudo apt update && sudo apt upgrade -y
sudo apt install build-essential dkms
```

``` bash
wget https://us.download.nvidia.com/tesla/535.104.12/nvidia-driver-local-repo-ubuntu2204-535.104.12_1.0-1_arm64.deb
```

``` bash
sudo apt install ./nvidia-driver-local-repo-ubuntu2204-535.104.12_1.0-1_arm64.deb
```