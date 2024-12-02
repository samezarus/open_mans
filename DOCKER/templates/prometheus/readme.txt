run:

    https://prometheus.io/docs/prometheus/latest/installation/ 

    # Create persistent volume for your data
    docker volume create prometheus-data

    # Start Prometheus container
    docker run \
    -p 9090:9090 \
    -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
    -v prometheus-data:/prometheus \
    prom/prometheus

config:

    https://prometheus.io/docs/prometheus/latest/configuration/configuration/

    https://github.com/prometheus/prometheus/blob/main/documentation/examples/prometheus.yml