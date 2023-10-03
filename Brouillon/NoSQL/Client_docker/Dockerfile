FROM debian:latest

RUN apt-get update && \
    apt-get install -y mongodb-clients && \
    apt-get clean
    useradd -ms /bin/bash user


USER user
WORKDIR /home/user

#CMD ["mongo"]
CMD ["bash"]
