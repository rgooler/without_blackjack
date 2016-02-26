FROM gliderlabs/alpine:latest

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

WORKDIR /myapp

ONBUILD COPY . /myapp
ONBUILD RUN virtualenv /env && /env/bin/pip install -r /myapp/requirements.txt

EXPOSE 8080
CMD ["/env/bin/python", "main.py"]
