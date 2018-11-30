FROM python:3.6-alpine

WORKDIR /$APP_HOME

COPY . $APP_HOME/
RUN pip3 install -e .

CMD python3 src/iSecurityWebServer/webserver.py