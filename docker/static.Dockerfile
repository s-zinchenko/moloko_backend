ARG PYTHON_VERSION=3.10-slim

FROM python:${PYTHON_VERSION} as builder
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc git
RUN pip install -U pip setuptools wheel
ARG PIP_EXTRA_INDEX_URL

WORKDIR /wheels
COPY requirements /requirements
RUN pip install -r /requirements/main.txt

WORKDIR /code
COPY . .
RUN python manage.py collectstatic --noinput

FROM nginx:alpine
COPY --from=builder /code/static/ /usr/share/nginx/html/dj_static
EXPOSE 80 80
