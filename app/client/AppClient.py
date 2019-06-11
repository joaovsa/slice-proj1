import requests
from datetime import datetime

# Método POST
data = {'info': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
r = requests.post('http://198.162.50.2:5000/', json=data)
print("POST ENVIADO OK > {}".format(r.json()))

# Método GET
r = requests.get('http://198.162.50.2:5000/')
print("GET OK > {}".format(r.json()))

