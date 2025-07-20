FROM python:3.13.5-slim AS builder

RUN apt-get update && apt-get install -y make

RUN pip install --upgrade pip && pip install uv

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml .

RUN uv sync

FROM python:3.13.5-slim

ENV PYTHONPATH="${PYTHONPATH}:/app/src"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/bin/make /usr/bin/make

COPY . .