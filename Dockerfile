# FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
# RUN apk --update add bash nano
# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static
# COPY ./requirements.txt /var/www/requirements.txt
# RUN pip install -r /var/www/requirements.txt
FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app
RUN pip install -r /app/requirements.txt