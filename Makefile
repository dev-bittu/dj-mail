.PHONY: *

mm:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

setup:
	pip install -r requirements.txt
	@make mm
	@make superuser

run:
	python manage.py runserver

test:
	python manage.py test

freeze:
	pip freeze > requirements.txt

push:
	@make freeze
	git push -u origin main

clean:
	rm -rf ./*/migrations/00*.py
	rm -rf ./*/__pycache__/*
	rm -rf ./*/utils/__pycache__/*
	rm -rf ./*/migrations/__pycache__/*.pyc

cleandb:
	rm -rf db.sqlite3
	@make clean
	@make mm
	@make superuser