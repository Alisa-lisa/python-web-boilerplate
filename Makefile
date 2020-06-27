default: init

init:
	poetry install

test: init
	poetry run pytest

lint: init
	poetry run flake8

.PHONY: docker-run
docker-run:
	docker-compose up --build -d 

.PHONY: docker-clean
docker-clean:
	docker-compose down
