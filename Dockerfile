FROM python:3.8.13-slim-buster

MAINTAINER github/jackanakin

EXPOSE 8000

WORKDIR /opt
RUN mkdir /opt/json

COPY /src src
COPY pip_install.txt .

RUN pip install --upgrade pip
RUN pip install -r pip_install.txt

ENTRYPOINT ["python", "/opt/src/http-server.py"]
