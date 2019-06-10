#!/bin/bash
#Script para configurar a VM Master


#Instalando o Docker
sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
sudo apt -y upgrade

#baixa repositorio e entra na pasta
git clone https://github.com/joaovsa/slice-proj1
cd slice-proj1/app/server

#Iniciando o Docker Swarm Master na VM Master
sudo docker swarm init --advertise-addr 192.168.50.2:2377 | sed 5!d > /vagrant/join.sh


#Cria imagem do Dockerfile no container
docker build -t py_server .

#docker port foward <host>:<container>
#roda em processo separado p/ não travar o cmd
#testar post via cmd curl -d 'info=blabla' <endereco>
docker run -p 5000:5000 py_server &

#criar docker service