FROM python:3.11-buster as builder

RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Required for poetry to work
RUN touch README.md

RUN poetry install --with api --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY src ./src

RUN poetry build

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    DIST_FOLDER=/app/dist \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=builder ${DIST_FOLDER} ${DIST_FOLDER}

RUN pip install /app/dist/*.whl

COPY api ./api
COPY mkdocs.yml ./

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0"]
