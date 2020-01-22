FROM alexstefanescu/catpol-dependencies

RUN pip3 install --upgrade pip setuptools

ARG ENVIRONMENT=dev
ENV DJANGO_SETTINGS_MODULE=project_template.settings.${ENVIRONMENT}

# RUN find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
#     rm -rf ~/.cache/pip

COPY . /opt/catpol
RUN python3 manage.py check
CMD python3 manage.py migrate --run-syncdb \
    && python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000
