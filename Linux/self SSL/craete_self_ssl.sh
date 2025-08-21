OUTPUT_PATH=~./self_ssl
KEY_FILE=cert.key
CRT_FILE=cert.crt
DAYS=99999

mkdir -p ${OUTPUT_PATH}

sudo openssl req -x509 -nodes -days ${DAYS} -newkey rsa:2048 -keyout ${OUTPUT_PATH}/${KEY_FILE} -out ${OUTPUT_PATH}/${CRT_FILE}
