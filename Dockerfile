FROM python:3.8-alpine
LABEL rawheel sid

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# copying to app dir in container
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -D is for that user can only user our processes but don't get root access
RUN adduser -D user
USER user