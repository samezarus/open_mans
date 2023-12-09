from os import environ

APP_VERSION = "v1.0.0 beta 7"
LCM_DEFAULT_MODEL = "SimianLuo/LCM_Dreamshaper_v7"
LCM_DEFAULT_MODEL_OPENVINO = "deinferno/LCM_Dreamshaper_v7-openvino"
APP_NAME = "FastSD CPU"
APP_SETTINGS_FILE = "settings.yaml"
RESULTS_DIRECTORY = "results"
CONFIG_DIRECTORY = "configs"
DEVICE = environ.get("DEVICE", "cpu")
