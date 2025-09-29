https://www.keycloak.org/ 


docker run \
-p 8080:8080 \
-e KEYCLOAK_USER=admin \
-e KEYCLOAK_PASSWORD=admin \
quay.io/keycloak/keycloak:11.0.0