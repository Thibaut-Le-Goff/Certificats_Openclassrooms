FROM debian:latest

RUN apt-get update && \
    apt-get install -y mongodb-clients && \
    apt-get clean

WORKDIR /app

CMD ["mongo"]
