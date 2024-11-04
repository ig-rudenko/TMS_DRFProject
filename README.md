## TMS проект Django REST Framework


## Документация

[Принципы REST API](docs/REST.drawio.pdf)

[Django token auth](docs/django-token-auth.pdf)

[Django JWT](docs/django-jwt-auth.pdf)

[Способы авторизаций](docs/JWT.pdf)

[Django Cache](docs/Django%20Cache.svg)

[Детальная схема DRF CBV](docs/drf-cbv.drawio.pdf)


## Задания

[Задание 1. Приложение Events](docs/ex1.pdf)

[Задание 2. Приложение Events](docs/ex2.pdf)

[Задание 3. Приложение Events. Celery](docs/ex3-celery.pdf)


## Запуск Celery

Worker (Email):

```shell
celery -A TMS_DRFProject.celery:app worker -l info -P eventlet -Q email
```

Beat:

```shell
celery -A TMS_DRFProject.celery:app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

Flower:

```shell
celery -A TMS_DRFProject.celery:app flower --port=5555
```