Консольные утилиты:
	nvidia-smi
	
	nvtop


-----------------------------------------------------------------------------------------------------------------------------------------------------------

Вывод устройств nvidia:

	lspci | grep -i nvidia

-----------------------------------------------------------------------------------------------------------------------------------------------------------

CUDA Toolkit:
	https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

	11.8:
		nvidia p40/p100

		https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local
		
		pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
		
		wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
		sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
		wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
		sudo dpkg -i cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
		sudo cp /var/cuda-repo-ubuntu2204-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
		sudo apt-get update
		sudo apt-get -y install cuda

	12.8:
		https://developer.nvidia.com/cuda-12-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local
	
	Самая свежая версия:
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
