FROM debian:jessie AS BACK_DFC

MAINTAINER Courtel Eliot <eliot.courtel@wanadoo.fr>

RUN apt-get update && apt-get install curl -y
RUN cd ~ && curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install nodejs build-essential -y
RUN npm install -g pm2
RUN apt-get install python3 python3-pip -y
RUN apt-get install git -y
RUN pip3 install requests bottle gitpython
RUN apt-get install openssh-client
RUN mkdir /home/api
RUN apt-get install nano

ENTRYPOINT cd /home/api/ && \
	   if [ "$PROD" -eq 1 ]; then rm -r DialogFlowAutoCorrect/back-end; mkdir tmp; cd tmp; git clone --quiet https://github.com/SCcagg5/DialogFlowAutoCorrect > /dev/null; cd ..; mv tmp/DialogFlowAutoCorrect/back-end DialogFlowAutoCorrect/back-end; fi && \
	   cd ./DialogFlowAutoCorrect/back-end/src && pm2 start --interpreter python3 server.py --watch > /dev/null & > /dev/null;\
	   cd /home/ > /dev/null &&\
	   git clone https://github.com/SCcagg5/DialogFlowModule > /dev/null && \
	   cd DialogFlowModule && git config --global credential.helper store > /dev/null && \
	   git config --global user.email "sccagg5@gmail.com" > /dev/null &&\
	   git config --global user.name "API" > /dev/null &&\
	   git config --global push.default matching > /dev/null &&\
	   git commit -m "initialisation" > /dev/null ;\
	   /bin/bash
