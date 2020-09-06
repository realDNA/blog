FROM ubuntu:20.04
MAINTAINER Aaron Wei.

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

EXPOSE 8000

# Setup directory structure
RUN mkdir /blog_root
WORKDIR /blog_root/blog/

COPY blog/requirements/base.txt /blog_root/base.txt
COPY blog/requirements/dev.txt /blog_root/requirements.txt

# install Python 3
RUN apt-get update && apt-get install -y \
        software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip
RUN python3.8 -m pip install pip
RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-setuptools

# install Postgresql
RUN apt-get -y install curl ca-certificates gnupg
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main 13" > /etc/apt/sources.list.d/pgdg.list'
RUN apt-get update
RUN apt-get -y install postgresql-client-13


# Install some dep
RUN apt-get install net-tools
RUN apt-get install -y libpq-dev python-dev

RUN pip3 install -r /blog_root/requirements.txt

# Copy application
COPY ./blog/ /blog_root/blog/

RUN apt-get update && apt-get -y install vim