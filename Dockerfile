FROM python:3.7
MAINTAINER Arseny Sokolov <me@arsen.pw>

# Зададим переменные окружения
ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.6.1
ENV DJANGO_SETTINGS_MODULE mandarhan.settings

RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    libopenjp2-7-dev \
    sqlite3 \
    locales \
    cron \
    postgresql-client \
    gettext \
    wget

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Установим дополнительные необходимые зависимости
RUN pip install --upgrade pip && pip install pipenv gunicorn

# Создадим requirements.txt для установки пакетов python
COPY Pipfile* /
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

# Скопируем проект в рабочую директорию
COPY . /usr/src/app

# Установим рабочую директорию
WORKDIR /usr/src/app

ENTRYPOINT ["./entrypoint.sh"]
CMD ["runserver", "0.0.0.0:8000"]
