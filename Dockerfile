ARG PYTHON_VERSION=3.5.7-alpine3.10
FROM python:${PYTHON_VERSION}

ARG ENVIRONMENT=dev
ENV DJANGO_SETTINGS_MODULE=project_template.settings.${ENVIRONMENT}

RUN apk add --no-cache \
    --virtual .build-deps \
    git
WORKDIR /opt/catpol
COPY ./requirements* /opt/catpol/
RUN pip3 install -r requirements-${ENVIRONMENT}.txt \
    && apk del .build-deps

COPY . /opt/catpol
RUN python3 manage.py check
CMD python3 manage.py migrate \
    && python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000
