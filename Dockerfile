# pull official base image
FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /usr/src/app


# Install pkg-config, MariaDB libraries, gcc (for compiling extensions), and build-essential
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    gcc

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/