#export COMPOSE_PROJECT_NAME ?= djangoboi
export COMPOSE_FILE = docker-compose.yml:docker/docker-compose.local.yml

up:
	$(info Launching the database + server...)
	@docker-compose up -d database
	@docker-compose up server

down:
	$(info Removing the database + server containers...)
	@docker-compose down

nuke:
	$(info Purging all database + server containers, images, networks, volumes...)
	@docker-compose down -v --rmi all

bash:
	$(info Shelling into the server...)
	@docker-compose exec server bash
