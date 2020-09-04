
# Put this file in the root of your app, next to the requirements.txt.
# This image includes multiple ONBUILD triggers which should cover most applications. 
# The build will COPY . /usr/src/app, RUN pip install, EXPOSE 8000, and set the default command to python manage.py runserver.

# MongoDB Dockerfile
#
# https://github.com/dockerfile/mongodb
#

# Pull base image.
FROM ubuntu:16.04

RUN apt-get -y update
RUN apt-get -y install python-pip
  
WORKDIR /usr/src/hub
COPY Hub/ .
COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /usr/src/hub/ecointeraction
RUN python ./manage.py migrate
RUN python ./manage.py runscript generateClassification
RUN python ./manage.py makemigrations

  
  
EXPOSE 8000

CMD python ./manage.py runserver 0.0.0.0:8000