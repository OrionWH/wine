FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

#-- install some packages --------------------------------------------------------------
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  vim \
  git \
  curl \
  wget \
  iproute2 \
  python3 \
  python3-pip

RUN  pip3 install requests

WORKDIR /data/wine