default: mk mi cac su mock
docker: b tag p
b:
	docker build -t agrifile:latest -f Dockerfile .
p:
	docker push 0x7c/agrifile

tag:
	docker tag agrifile:latest 0x7c/agrifile:latest

r:
	python manage.py runserver

ru:
	python manage.py runserver_plus 0.0.0.0:8000 --keep-meta-shutdown

sh:
	python manage.py shell_plus

cl:
	rm -rf ./storage/*
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
mk:
	python manage.py makemigrations

mi:
	python manage.py migrate

cac:
	python manage.py createcachetable

mock:
	echo "from django.contrib.auth import get_user_model;from set; from setmeup.models import LichBaoCao, NoiNhan, PhongBan, Title; User = get_user_model(); User.objects.create_superuser(username='admin', password='admin123', phongban=PhongBan.objects.last(), title=Title.objects.last())" | python manage.py shell

mock:
	python manage.py mock_alias
#	python manage.py shell < user/mocks.py
#	python manage.py shell < heo/mocks.py

test:
	#python manage.py makemigrations --dry-run | grep 'No changes detected' || (echo 'There are changes which require migrations.' && exit 1)
	coverage erase && coverage run --source='.' manage.py test && coverage htm && coverage report -m --fail-under 100

beat:
	celery -A chuthe beat -l INFO

worker:
	celery -A chuthe worker -l INFO -Ofair --concurrency=4 -P eventlet -c 1000 --without-gossip --without-mingle --without-heartbeat
