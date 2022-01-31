FROM python:3.8-alpine

COPY requirements.txt /app/

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip3 install --no-cache -r requirements.txt

COPY . .

EXPOSE 1883

CMD [ "python3", "-u", "/app/mqtt_publisher.py", "/app/mqtt_publisher_conf.json" ]
