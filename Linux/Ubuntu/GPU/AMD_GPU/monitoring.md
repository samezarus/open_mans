# Мониторинг

## radeontop

``` bash
sudo apt install -y radeontop
radeontop
```

## rocm-smi

``` bash
sudo apt install -y rocm-smi
```

## amdgpu_top

- Установка

``` bash
sudo apt install libdrm-tests
```

- Сборка

``` bash
git clone https://gitlab.freedesktop.org/mesa/drm.git
cd drm
meson build
ninja -C build
sudo ninja -C build install
```