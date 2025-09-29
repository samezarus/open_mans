CNTR=wireguard

up:
	docker-compose up -d

down:
	docker-compose down -v
	
qr:
	docker exec -it $(CNTR) /app/show-peer 1
