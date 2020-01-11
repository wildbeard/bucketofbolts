FROM python:3.7-alpine

COPY ./start.sh /var/www/bucketofbolts/

RUN chmod +x /var/www/bucketofbolts/start.sh

EXPOSE 80

ENTRYPOINT [ "/var/www/bucketofbolts/start.sh" ]