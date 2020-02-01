FROM alexstefanescu/catpol-dependencies

RUN pip3 install --upgrade pip setuptools \
    && wget -qO- https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz | tar -zxf - -C /usr/bin \
    && chown root:root /usr/bin/dockerize

ARG ENVIRONMENT=dev
ENV DJANGO_SETTINGS_MODULE=project_template.settings.${ENVIRONMENT}

COPY ./ /opt/catpol

# Re-install dependencies since it might have updated from cache
RUN pip3 install -r requirements-${ENVIRONMENT}.txt

RUN python3 manage.py check

ENTRYPOINT ["/opt/catpol/docker-entrypoint"]
EXPOSE 8000
