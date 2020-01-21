FROM ubuntu:18.04

MAINTAINER SRIPAAD SRINIVASAN "sripaad751@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt
COPY . /app

WORKDIR /app

# RUN pip3 install -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]
