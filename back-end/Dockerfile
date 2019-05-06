FROM debian:jessie AS BACK_DFC

LABEL maintainer="Courtel Eliot"
LABEL maintainermail="eliot.courtel@wanadoo.fr"

RUN apt-get update --no-install-recommends && apt-get install curl -y --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN cd ~ && curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install nodejs build-essential -y --no-install-recommends
RUN npm install -g pm2
RUN apt-get install python3 python3-pip -y --no-install-recommends
RUN apt-get install git -y --no-install-recommends
RUN pip3 install requests bottle uuid
RUN easy_install3 -U pip 
RUN pip install google-cloud-language
RUN apt-get install openssh-client -y --no-install-recommends
RUN mkdir /home/api
RUN apt-get install nano -y --no-install-recommends
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ENTRYPOINT cd /home/api/ && \
	   if [ "$PROD" -eq 1 ];then mkdir prod; cd prod; git clone --quiet https://github.com/SCcagg5/DialogFlowAutoCorrect > /dev/null; fi && \
	   cd ./DialogFlowAutoCorrect/back-end/src && pm2 start --interpreter python3 server.py --watch > /dev/null & > /dev/null;\
	   cd /home/ > /dev/null &&\
	   git clone https://github.com/SCcagg5/DialogFlowModule > /dev/null && \
	   cd DialogFlowModule && git config --global credential.helper store > /dev/null && \
	   git config --global user.email "sccagg5@gmail.com" > /dev/null &&\
	   git config --global user.name "API" > /dev/null &&\
	   git config --global push.default matching > /dev/null &&\
	   git commit -m "initialisation" > /dev/null ;\
	   /bin/bash
