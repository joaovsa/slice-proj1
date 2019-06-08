import requests

# Método GET
r = requests.get('http://localhost:5000/')
print(r.json())

# Método POST
data = {'info': 'teste'}
r = requests.post('http://localhost:5000/info', json=data)
print(r.json())