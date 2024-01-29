# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app
ENV FLASK_APP lab_flask/app.py

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "lab_flask/app.py"]