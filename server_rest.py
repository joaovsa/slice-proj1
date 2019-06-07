from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

languages =[
    {'name': 'JavaScript'},
    {'name': 'Python'},
    {'name': 'Ruby'}
    ]

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'It work!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    lang = [lang for lang in languages if lang['name'] == name]
    return jsonify({'language': lang})

@app.route('/lang', methods=['POST'])
def addOne():
    lang = {'name': request.json['name']}
    languages.append(lang)
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(host='localhost', port='5000')