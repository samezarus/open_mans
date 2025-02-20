Создание:

    sudo mkdir -p /etc/ssl/self-signed
    cd /etc/ssl/self-signed

    sudo openssl genpkey -algorithm RSA -out private.key -aes256

    sudo openssl req -new -x509 -key private.key -sha256 -days 365 -out certificate.crt

    openssl x509 -in certificate.crt -text -noout


----------------------------------------------

Удаление пароля у ключа:

    sudo cp /etc/ssl/self-signed/private.key /etc/ssl/self-signed/private.key.backup

    sudo openssl rsa -in /etc/ssl/self-signed/private.key -out /etc/ssl/self-signed/private.key.unencrypted

    sudo mv /etc/ssl/self-signed/private.key.unencrypted /etc/ssl/self-signed/private.key

    sudo chmod 600 /etc/ssl/self-signed/private.key