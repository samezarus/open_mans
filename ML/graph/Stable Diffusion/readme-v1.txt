https://www.assemblyai.com/blog/how-to-run-stable-diffusion-locally-to-generate-images/

--------------------------------------------------------------------------------------

Для GPU:


Для CPU: 

    обязательно ставить Miniconda3-py38_4.12.0-Linux-x86_64.sh

    активировать окружение Miniconda3 (в начале строки должна появиться надпись "(base)"):
        conda activate
        или
        переоткрыть консоль 

    использовать интерпритатором Miniconda:
        /home/<user>/miniconda3/bin/python
        
    установка зависимостей (в Miniconda): 
        cd <path>./stable_diffusion.openvino/
        /home/<user>/miniconda3/bin/python -m pip install -r requirements.txt
--------------------------------------------------------------------------------------

если ругается на ".cv2":
    /home/<user>/miniconda3/bin/python -m pip install opencv-python-headless==4.5.3.56

--------------------------------------------------------------------------------------

старот рендеринга:

    cd <path>./stable_diffusion.openvino/

    /home/<user>/miniconda3/bin/python3 demo.py --prompt "bright beautiful solarpunk landscape, photorealism"

--------------------------------------------------------------------------------------