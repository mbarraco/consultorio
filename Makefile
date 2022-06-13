.PHONY : bash migrate migrations reset shell superuser

bash:
	docker-compose run --rm web /bin/bash

compile:
	docker-compose run --rm web bash -c "pip-compile requirements.in"
	
consume:
	docker-compose run --rm web python consultorio/cli/main.py consume

migrate:
	docker-compose run --rm web python consultorio/manage.py migrate

migrations:
	docker-compose run --rm web python consultorio/manage.py makemigrations patients

reset: migrate superuser

setup: migrate superuser

shell:
	docker-compose run --rm web bash

django-shell:
	docker-compose run --rm web python consultorio/manage.py shell -i ipython


superuser:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('alejandro', 'admin@test.com', 'ale1234')" | docker-compose run --rm web python consultorio/manage.py shell

up:
	docker-compose up -d; 
