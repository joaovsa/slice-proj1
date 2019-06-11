import requests
from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime #builtin
import json #builtin

app = Flask(__name__)
api = Api(app)

class SysInfo(Resource):	
    COUNTER = 0
    
    def post(self):
		try:
            data = request.get_json()
            stats = data['info']
            print("POST solicitado ao cli endpoint, enviando...\n")
            self.oper(1, stats)
        except:
            data = request.get_json()
            id = data['id']
            print("GET solicitado ao cli endpoint, obtendo...\n")
            self.oper(2, id)

	def oper(self, opt, stri):
        if opt == 1:# Método POST
            data = {'id': str(COUNTER),\
                'info': stri}
            r = requests.post('http://192.168.50.2:2377/', json=data)
            print("<CLI endpoint> POST ENVIADO OK > {}".format(r.json()))
            SysInfo.COUNTER += 1
        elif opt == 2:            
            # Método GET
            r = requests.get('http://192.168.50.2:2377/')
            print("<CLI endpoint> GET OK > {}".format(r.json()))

		

api.add_resource(SysInfo, '/')

if __name__ == '__main__':
    print('Running flask cli endpoint')
    app.run(host='0.0.0.0', port='5000', debug=True)

