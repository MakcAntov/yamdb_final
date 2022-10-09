FROM python:3.7-slim

WORKDIR /app

COPY ../api_yamdb/ .

RUN pip install -r requirements.txt

CMD python manage.py runserver 0:5000