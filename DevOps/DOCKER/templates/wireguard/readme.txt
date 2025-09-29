https://igancev.ru/2021-02-21-vpn-wireguard-docker

Чтобы вывести на экран qr код добавления туннеля, на сервере исполняем команду:
	docker exec -it wireguard /app/show-peer 1
	
	Где 1 - порядковый номер PEERS, количество которых мы ранее задали в docker-compose.yml
