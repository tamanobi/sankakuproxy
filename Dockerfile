FROM python:3.9-buster as builder

WORKDIR /opt/app

RUN pip install poetry && poetry config virtualenvs.in-project false && poetry config virtualenvs.create false
COPY prox/poetry.lock prox/pyproject.toml /opt/app/
RUN poetry install 

FROM python:3.9-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

RUN apt update \
  && apt install -y libpq5 libxml2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -r -s /bin/false uvicornusr
RUN mkdir -p /opt/app/src/logs/app_logs
RUN touch /opt/app/src/logs/server.log
RUN chown -R uvicornusr /opt/app/src/logs

USER uvicornusr
WORKDIR /opt/app

EXPOSE 8000
