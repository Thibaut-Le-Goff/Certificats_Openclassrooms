FROM mongo:latest

WORKDIR /data

COPY restaurants.json_.zip /data/

RUN apt-get update -y && apt-get install -y unzip
RUN unzip restaurants.json_.zip -d /data/
RUN rm restaurants.json_.zip

VOLUME [ "/data/db" ]

EXPOSE 27017

CMD ["mongod"]