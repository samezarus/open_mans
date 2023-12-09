OUTPUT_PATH=~/self_ssl/
KEY_FILE=my.key
CRT_FILE=my.crt

mkdir -p $OUTPUT_PATH

sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $OUTPUT_PATH$KEY_FILE -out $OUTPUT_PATH$CRT_FILE
