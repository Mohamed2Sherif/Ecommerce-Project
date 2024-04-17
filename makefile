# Makefile for managing Django project with Docker Compose

# Variables
COMPOSE_FILE := compose_local.yml

# Commands
.PHONY: run start stop restart logs push

run: start logs

start:
	@docker-compose -f $(COMPOSE_FILE) up -d --build

stop:
	@docker-compose -f $(COMPOSE_FILE) down

restart: stop start

logs:
	@docker-compose -f $(COMPOSE_FILE) logs -f

push:
	git push && git push --tags