FROM debian:jessie AS Crazy_Coach_api

MAINTAINER Courtel Eliot <eliot.courtel@wanadoo.fr>

RUN apt-get update && apt-get install curl -y
RUN cd ~ && curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install nodejs build-essential -y
RUN npm install -g pm2
RUN apt-get install python3 python3-pip -y
RUN apt-get install git -y
RUN mkdir /home/api

ENTRYPOINT cd /home/api/ && \
	   git clone --quiet https://github.com/SCcagg5/DialogFlowAutoCorrect > /dev/null && \
	   cd ./DialogFlowAutoCorrect/back-end/src && \
	   cat dependencies.txt | while read ligne; do pip3 install $ligne ; done \
	   && pm2 start --interpreter python3 server.py && /bin/bash