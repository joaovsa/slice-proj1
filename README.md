# Trabalho prático p/ disciplina de TAAD
## UFSCar - Campus Sorocaba - 2019/1
Docente: Fábio Verdi

Auxiliares: André Beltrami e Paulo Ditarso


### Objetivo:
 Criação automatizada de duas VMs do Vagrant com container docker instalado. Numa VM haverá um container com aplicação python assumindo papel de servidor, e na segunda VM uma aplicação containerizada com a aplicação cliente, que faz requisições HTTP (GET e POST) para o servidor.


### Instruções
Exemplos baseados a partir da aula prática 2. Fonte: https://github.com/dcomp-leris/slice-enablers/aula2

## Passo 1:
 Instalar o VirtualBox e o Vagrant

```markdown
 $ sudo apt update
 $ sudo apt install virtualbox
 $ sudo apt install vagrant
```

## Passo 2:
Clonar este repositório e acessar a pasta /vm

```markdown
 $ git clone https://github.com/joaovsa/slice-proj1.git
 $ cd slice-proj1/vm
```

## Passo 3:
Verificar e iniciar as VMs. As etapas de instalação e configuração do docker são feitas por scripts sendo executados durante a criação das VMs via Vagrantfile.

```markdown
 $ vagrant status
 $ cat Vagrantfile
 $ vagrant up
```

## Passo 4:
Acessar a VM master e iniciar outro terminal para acessar a VM worker.

```markdown
 $ vagrant ssh master
 
 #Em outro terminal
 $ vagrant ssh worker
```

## Passo 5:
 Acessar a pasta slice-proj1/app/client e executar o container docker já gerado automaticamente na VM:

```markdown
 vagrant@worker$ sudo docker run -t py_client
```
## Saída
A saída representa 10 tentativas de POST e GET do client para  o servidor. O servidor armazena os posts do client (timestamps), e ao ser solicitado via GET, devolve um JSON com todos os timestamps recebidos via POST.


## Considerações e Dificuldades
O projeto foi de grande aprendizado para os integrantes do grupo, de tal modo que se tornaram familiares no que diz respeito às tecnologias habilitadoras de cloud networking. Desse modo, estão aptos a utilizar Docker ou Vagrant em soluções simples do dia a dia. 

Para este projeto, a maior dificuldade foi entender os níveis de virtualização e até que ponto era necessário o aninhamento deles. De modo similar, a estrutura do Docker no modo swarm causou questionamento entre os integrantes, já que containers de VMs diferentes foram agrupados no mesmo grupo Swarm. 
Quanto às dificuldades técnicas do modo swarm, o grupo optou por criar um arquivo acessível em ambas as VMs, com uma chave para entrar no cluster, ao invés de baixar o arquivo entre as VMs, via comando scp. Isso deve-se ao fato da dificuldade de configurar uma conexão SSH para utilizar um arquivo compartilhado. Nós entendemos que essa abordagem compromete a segurança e o foco deste trabalho consiste em exercitar o conhecimento recém-adquirido.

O grupo não criou requisições que transportam "docker stats" do container cliente, porque não conseguiu executar a imagem docker do servidor, a partir de um script Pyhon, para obtermos o  <img id> do Docker, a fim de utilizarmos o respectivo método fornecido pelo [Docker Python SDK](https://docker-py.readthedocs.io/en/stable/) que requer tal parâmetro. O arquivo que executaria a imagem Docker (cli_boot.py) e o servidor cliente que estaria dentro da imagem para enviar requisições ao master (AppClient_old.py), ainda estão no repositório para fins de desenvolvimento futuro. 