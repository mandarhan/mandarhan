=================================
Mandarhan Hotel Management System
=================================

.. role:: bash(code)
   :language: bash

Установка на сервер
###################

1. :bash:`git clone https://github.com/mandarhan/mandarhan.git`
2. :bash:`docker-compose build --pull --force-rm`
3. :bash:`docker-compose run --rm django python manage.py collectstatic --no-input`
4. :bash:`docker-compose --detach`


Обновление сервера
##################

1. :bash:`docker-compose stop`
2. :bash:`git pull`
3. :bash:`docker-compose build --no-cache --force-rm --pull`
4. :bash:`docker-compose run --rm django python manage.py collectstatic --no-input`
5. :bash:`docker-compose --detach`
