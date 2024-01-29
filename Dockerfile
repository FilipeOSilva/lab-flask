# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
ENV FLASK_APP lab_flask/app.py

COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

RUN poetry install --without dev

ENTRYPOINT ["poetry", "run", "python", "lab_flask/app.py"]
# CMD ["python3", "lab_flask/app.py"]