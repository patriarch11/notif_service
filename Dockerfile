FROM python:3.10-alpine

RUN apk add --no-cache gcc musl-dev

WORKDIR /app

COPY notification_service /app/notification_service
COPY .env app
COPY pyproject.toml poetry.lock /app/

COPY README.md /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

CMD ["python", "notification_service/main.py"]