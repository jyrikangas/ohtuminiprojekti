# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Configure Poetry
ENV POETRY_VERSION=1.2.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /src/

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . /src

WORKDIR /src/src

RUN python3 src/init_db.py

EXPOSE 5000

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
