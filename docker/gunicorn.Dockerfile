ARG PYTHON_VERSION=3.10-slim


FROM python:${PYTHON_VERSION} as builder
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc git
RUN pip install -U pip setuptools wheel
ARG PIP_EXTRA_INDEX_URL

WORKDIR /wheels
COPY requirements /requirements
RUN pip wheel -r /requirements/main.txt


FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1

COPY --from=builder /wheels /wheels
RUN pip install -U pip
RUN pip install /wheels/* \
        && rm -rf /wheels \
        && rm -rf /root/.cache/pip/*

WORKDIR /code
COPY . .

EXPOSE 8000
ENV PYTHONPATH /code
CMD ["gunicorn", "-c", "docker/gunicorn.conf", "moloko_backend.application.wsgi:application"]
