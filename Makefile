include .env
.PHONY: init, restart, update

init:
	docker compose up -d --build

restart:
	docker compose restart app db

update:
	docker compose up app -d --build