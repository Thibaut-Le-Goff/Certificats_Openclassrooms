FROM mongo:latest

WORKDIR /data

RUN apt-get update -y && \
    apt-get clean 
    #&& \
    #useradd -ms /bin/bash user


#USER user
#WORKDIR /home/user

VOLUME ["/data/db"]

EXPOSE 27017:27017

CMD ["mongod"]

#
# Commandes pour démarer le contenaire
#

# docker build -t mongo_server MongoDB
# docker run mongo_server


#
# Commande pour exporter la basse de donnée au serveur (après avoir installer mongodb sur la machine hôte) :
#

# mongoimport --host=172.17.0.2:27017 --db new_york --collection restaurants restaurants.json
