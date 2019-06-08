from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

info_list = \
    [
        {'Horário da requisição': 'xpto',
    'Nome do container': 'xpto',
    'ID do container': 'xpto',
    'ID da imagem': 'xpto',
    'Uso de CPU': 'xpto',
    'Uso de Memória': 'xpto', }
    ]

@app.route('/', methods=['GET'])
def get_info():
    return jsonify({'info': info_list})

@app.route('/info', methods=['POST'])
def post_info():
    info = {'info': request.json['info']}
    info_list.append(info)
    print(info_list)
    return jsonify({'info': info_list})

if __name__ == '__main__':
    app.run(host='localhost', port='5000')