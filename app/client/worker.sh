#!/bin/bash
#Script para configurar a VM Worker

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
sudo gpasswd -a "${USER}" docker

#baixa repositorio e entra na pasta
git clone https://github.com/joaovsa/slice-proj1
cd slice-proj1/app/client

#Adiciona a permissão p/ join no Docker Swarm
chmod +x /vagrant/join.sh

#Adiciona o worker no Cluster Swarm c/ chave gerada pelo master
bash /vagrant/join.sh

#Cria imagem do Dockerfile no container
docker build -t py_client .
#run manual