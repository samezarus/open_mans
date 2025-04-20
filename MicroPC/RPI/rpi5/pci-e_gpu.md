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