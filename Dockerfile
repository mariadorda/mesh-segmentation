FROM python:3.8
RUN apt update
RUN apt -y install vim apt-utils cmake libeigen3-dev libcgal-dev swig
WORKDIR /app
RUN pip install --upgrade pip && pip install cgal