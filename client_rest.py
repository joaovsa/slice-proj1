import requests

r = requests.get('http://localhost:5000/')
print(r.json())

r = requests.get('http://localhost:5000/lang')
print(r.json())

r = requests.get('http://localhost:5000/lang/JavaScript')
print(r.json())

data = {'name': 'c++'}
r = requests.post('http://localhost:5000/lang', json=data)
print(r.json())

