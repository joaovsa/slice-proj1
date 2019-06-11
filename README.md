# Trabalho prático p/ disciplina de TAAD
## UFSCar - Campus Sorocaba - 2019/1
Docente: Fábio Verdi

### Objetivo:
 Criação de server e client envolvidos em containers Docker e controlados por Vagrant.

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
Verificar e iniciar as VMs. As etapas de instalação e configuração do docker são feitas por scripts sendo executados durante a criação das VMs.

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
 ...

```markdown
 $ ...
```

