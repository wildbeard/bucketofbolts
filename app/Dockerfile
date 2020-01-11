FROM python:3.7-alpine

COPY . /var/www/app

WORKDIR /var/www/app

RUN pip install -r requirements.txt

RUN chmod +x /var/www/app/start.sh

EXPOSE 80

CMD [ "/var/www/app/start.sh" ]

# ENTRYPOINT [ "sh start.sh" ]