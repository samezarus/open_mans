https://hub.docker.com/r/bitnami/moodle

MOODLE_USERNAME: Default: user
MOODLE_PASSWORD: Default: bitnami

Start:

    curl -sSL https://raw.githubusercontent.com/bitnami/containers/main/bitnami/moodle/docker-compose.yml > docker-compose.yml
    docker-compose up -d