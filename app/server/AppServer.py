from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime #builtin
import json #builtin

app = Flask(__name__)
api = Api(app)

class SysInfo(Resource):
	INFO_LIST = []

	def get(self):
		print("GET solicitado em {}".format(datetime.now().time()))
		return {'info': SysInfo.INFO_LIST}

	def post(self):
		info = request.get_json()
		print("POST recebido em {}\n".format(datetime.now().time(), json.dumps(info, indent=2)))
		SysInfo.INFO_LIST.append(info)
		return info

api.add_resource(SysInfo, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
