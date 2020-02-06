FROM ubuntu:18.04

MAINTAINER SRIPAAD SRINIVASAN "sripaad751@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

ARG AWS_ACCESS_KEY_ID=foobar
ARG AWS_SECRET_ACCESS_KEY=foobar

CMD [ "app/app.py" ]