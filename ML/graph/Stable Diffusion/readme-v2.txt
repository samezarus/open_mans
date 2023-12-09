https://github.com/AUTOMATIC1111/stable-diffusion-webui

apt-get update && apt-get install libgl1

Если ошибка:
	
	Cannot add middleware after an application has started, то:
		
		pip install fastapi==0.89.1
