import docker
import requests
client = docker.from_env()

id = client.container.run('py_client', 'container iniciado!')

print("0 - SAIR; 1 - POST; 2 - GET\n")
a = input()
while(a != 0):
    if a == 1:
        data = {'opt': '1', 'info': client.containers.get(id).stats(decode=True)}
        #r = requests.post('http://192.168.50.3:2378/', json=data)
        r = requests.post('http://localhost:5000', json=data)
    elif a== 2:
        data = {'opt': '2'}
        r = requests.post('http://localhost:5000/', json=data)

    print("0 - SAIR; 1 - POST; 2 - GET\n")
    a = input()
    docker run -d -p 2378:5000 flask-tutorial
