FROM python:3.8-alpine
LABEL rawheel sid

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copying to app dir in container
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -D is for that user can only user our processes but don't get root access
RUN adduser -D user
USER user