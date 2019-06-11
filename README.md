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
 $ cd slice-pro1/vm
```

## Passo 3:
Verificar e iniciar as VMs. As etapas de instalação e configuração do docker são feitas por scripts sendo executados durante a criação das VMs via Vagrantfile.

```markdown
 $ vagrant status
 $ cat Vagrantfile
 $ vagrant up
```

## Passo 4:
 Acessar a VM Master e iniciar outro terminal para acessar a VM Worker

```markdown
 $ vagrant ssh master
 
 #Em outro terminal
 $ vagrant ssh worker
```

## Passo 5:
 Acessar a pasta slice-proj1/app/client, e execute o container docker já gerado automaticamente na VM:

```markdown
 vagrant@worker$ sudo docker run -y py_client
```
## Saída
A saída representa 10 tentativas de POST e GET do client ao servidor. O servidor armazena os posts do client (timestamps), e ao ser solicitado de um GET, revolve um JSON com todos os timestamps recebidos por POST.


## Considerações e Dificuldades
O projeto foi de grande aprendizado para os integrantes do projeto, de tal modo e tornaram-se familiares nos níveis básicos no que tange tecnologias habilitadoras de cloud networking. Deste modo, estando aptos à utilizar soluções Docker ou Vagrant em soluções simples do dia a dia. 
Para este projeto, a maior dificuldade foi entender os níveis de virtualização e em até que ponto era necessário o aninhamento deles. De modo similar, a estrutura do docker no modo swarm causou questionamento entre os integrantes, já que containers de VMs diferentes foram agrupados no mesmo grupo Swarm. Quanto a dificuldades técnicas do modo swarm, o grupo optou por criar um arquivo acessível à ambas VMs, com a chave para entrar no grupo, ao invés de baixar o arquivo entre VMs através de uma conexão segura SSH através do scp. Isto deve-se ao fato da dificuldade de configurar uma conexão SSH em relação à utilizar um arquivo compartilhado. Entendemos que essa abordagem compromete a segurança, mas o foco deste trabalho é exercitarmos o conhecimento recém-adquirido.
Não conseguimos criar requisições que transportam "docker stats" do container cliente. Isto ocorreu porque não conseguimos executar a imagem docker do servidor através de um script python e obtermos o <img id> do docker a fim de utilizarmos o respectivo método fornecido pelo [Docker Python SDK](https://docker-py.readthedocs.io/en/stable/) que requer tal parâmetro. O arquivo python que executaria a imagem Docker, e o servidor cliente que estaria dentro da imagem p/ enviar requisições ao master, ainda estão no repositório para fins de desenvolvimento futuro. São eles cli_boot.py e AppClient_old.py
