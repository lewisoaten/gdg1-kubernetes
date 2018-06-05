FROM python:3.6.5-alpine3.7
MAINTAINER lewis@razorsecure.com

# Setup the directories for the applications we are going to build
RUN mkdir -p /web
WORKDIR /web

CMD ["python", "server.py"]

# Install dependencies
COPY requirements.txt /web/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /web
