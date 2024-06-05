# Use the official slim Python image from the Docker Hub
FROM python:3.12.3-slim-bullseye AS python-run-stage

ARG BUILD_ENVIRONMENT=local

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

ARG APPHOME=/app

WORKDIR ${APPHOME}

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY ./requirements/ ./requirements
RUN pip install --no-cache-dir -r ./requirements/${BUILD_ENVIRONMENT}.txt 

EXPOSE 8000

COPY ./compose/local/django/celery/worker/start.sh /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start.sh /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy the entire application
COPY . ${APPHOME}

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
