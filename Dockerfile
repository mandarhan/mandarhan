FROM python:3.7

# Зададим переменные окружения
ENV PYTHONUNBUFFERED 1

# Установим рабочую директорию
WORKDIR /usr/src/app

# Установим дополнительные необходимые зависимости
RUN pip install --upgrade pip && pip install pipenv gunicorn

# Создадим requirements.txt для установки пакетов python
COPY Pipfile* /usr/src/app/
RUN cd /usr/src/app && pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

# Скопируем проект в рабочую директорию
COPY . /usr/src/app
