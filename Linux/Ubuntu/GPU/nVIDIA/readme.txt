Консольные утилиты:
	nvidia-smi
	
	nvtop


-----------------------------------------------------------------------------------------------------------------------------------------------------------

Вывод устройств nvidia:

	lspci | grep -i nvidia

-----------------------------------------------------------------------------------------------------------------------------------------------------------

CUDA Toolkit:
	https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

	
	22.04:
		https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_network

	24.04:
		https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local

	wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
	sudo dpkg -i cuda-keyring_1.0-1_all.deb
	sudo apt-get update
	sudo apt-get -y install cuda

	export LD_LIBRARY_PATH=/usr/local/cuda-12.0/lib64:$LD_LIBRARY_PATH
	export CUDA_HOME=/usr/local/cuda-12.0
	
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Driver Installer

	sudo apt-get install -y cuda-drivers

	или

	sudo apt-get install -y nvidia-open

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Install Nvidia Drivers on Ubuntu 20.04

https://phoenixnap.com/kb/install-nvidia-drivers-ubuntu

Install Nvidia Driver via Command Line

	sudo apt search nvidia-driver
	
	sudo apt update
	
	sudo apt upgrade
	
	sudo apt install <name> (из apt search nvidia-driver, то что выделенно зелёным)
	
		sudo apt install nvidia-driver-510-server
	
	sudo reboot
	
	nvidia-smi
