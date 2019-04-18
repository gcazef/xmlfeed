MANAGE = docker-compose run web python /code/manage.py

mkm:
	$(MANAGE) makemigrations

flush:
	$(MANAGE) flush

migrate:
	$(MANAGE) migrate

install:
	docker build .
	$(MANAGE) migrate --noinput
	$(MANAGE) createsuperuser

fetch_orders:
	$(MANAGE) fetch_orders

run:
	docker-compose up

run_bg:
	docker-compose up -d --build

stop:
	docker-compose down

test:
	$(MANAGE) test
