FROM alpine:3.8

RUN apk add --no-cache python3 git && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

WORKDIR /$APP_HOME

COPY . $APP_HOME/

RUN pip3 install -r requirements.txt && pip3 install -e .

CMD python3 src/isecurity_webserver/webserver.py