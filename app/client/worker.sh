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

#Copia o arquivo token.txt da VM Master
scp master@192.168.50.2:token.txt /home/vagrant

#Executando o token gerado pela VM Master para se juntar como Worker
source token.txt

#baixa repositorio e entra na pasta
git clone https://github.com/joaovsa/slice-proj1
cd slice-proj1/app/client

#Cria imagem do Dockerfile no container
docker build -t py_client .
#run manual