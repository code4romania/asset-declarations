FROM python:3.5.7-alpine3.10
RUN apk add git
WORKDIR /opt/catpol
COPY ./requirements* /opt/catpol/
RUN pip3 install -r requirements-dev.txt
COPY . /opt/catpol
ENV DJANGO_SETTINGS_MODULE=project_template.settings.dev
RUN python3 manage.py migrate 
CMD python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000