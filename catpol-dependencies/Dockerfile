FROM python:3.7.4-alpine

RUN apk update && \
    apk add --no-cache --virtual build-deps \
    gcc python-dev musl-dev \
    postgresql-dev git \
    build-base python3-dev openblas-dev \
    freetype-dev pkgconfig gfortran \
    bash

RUN pip3 install --upgrade pip setuptools

ARG ENVIRONMENT=dev

WORKDIR /opt/catpol
COPY ./requirements* /opt/catpol/
RUN pip3 install -r requirements-${ENVIRONMENT}.txt 

# RUN find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
#     rm -rf ~/.cache/pip