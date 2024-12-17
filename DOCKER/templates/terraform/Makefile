init:
	docker compose run --rm terraform init

validate:
	docker compose run --rm terraform validate

plan:
	docker compose run --rm terraform plan

apply:
	docker compose run --rm terraform apply

destroy:
	docker compose run --rm terraform destroy

up:
	docker compose up -d

down:
	docker compose down

restart: down up

rebuild:
	docker compose build --no-cache

logs:
	docker logs -f terraform

console:
	docker exec -it terraform /bin/sh