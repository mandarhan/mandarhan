#!/usr/bin/env bash

wait_for_db() {
  if [ -z "$POSTGRES_HOST" ]; then
    echo "No Django database host, not waiting for db."
  else
    echo "Waiting for database"
    dockerize -wait tcp://"$POSTGRES_HOST":5432 -timeout 30s
  fi
}

if [ "$1" == "runserver" ]; then
  exec gunicorn mandarhan.wsgi:application --bind "${@:2}"
elif [ "$1" == "init" ]; then
  wait_for_db
  python manage.py migrate
  python manage.py collectstatic --noinput
  python manage.py createsuperuser
elif [ "$1" == "update" ]; then
  wait_for_db
  python manage.py migrate
  python manage.py collectstatic --noinput
else
  exec "$@"
fi
