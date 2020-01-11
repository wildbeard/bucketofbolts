FROM python:3.7-alpine

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

EXPOSE 80

ENTRYPOINT [ "/start.sh" ]