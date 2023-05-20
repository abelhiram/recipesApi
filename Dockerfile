FROM python:3.9-alpine3.13
LABEL maintainer="abelhiram"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    #-----------install postgresql client in docker to use in app / this after configure compose.yml
    apk add --update --no-cache postgresql-client && \ 
    #group every file of instalation of postgresql to easily clean after
    apk add --update --no-cache --virtual .tmp-build-deps \ 
        build-base postgresql-dev musl-dev &&\
    #----------
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    #clean files in tmp-build-deps created in 
    apk del .tmp-build-deps &&\
    #--------------------------
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user