from flask import Flask,  jsonify, request
from Criptografia.criptografia.demo import *
import numpy as np
app = Flask(__name__)

@app.route('/para-one-hot', methods=['POST'])
# funcao que recebe uma mensagem e retorna a mensagem em one hot
def one_hot():
    # recebe a mensagem
    data = request.get_json()
    # pega a mensagem
    data = data['mensagem']
    # retorna a mensagem em one hot
    return jsonify({'mensagem_one_hot': str(para_one_hot(data))})
    

# funcao que recebe uma mensagem em one hot e retorna a mensagem
@app.route('/para-string', methods=['POST'])
def converte_para_string():
    data = request.get_json()
    data = np.array(data['mensagem'])
    print(data)
    return jsonify({'mensagem_string': para_string(data)})

# funcao que recebe uma mensagem e retorna a mensagem cifrada
@app.route('/cifrar', methods=['POST'])
def cifrar_mensagem():
    data = request.get_json()
    mensagem = data['mensagem']
    P = data['P']
    return jsonify({'mensagem_cifrada': cifrar(mensagem, P)})

# funcao que recebe uma mensagem cifrada e retorna a mensagem original
@app.route('/de-cifrar', methods=['POST'])
def desifrar():
    data = request.get_json()
    mensagem = data['mensagem']
    P = data['P']
    return jsonify({'mensagem_decifrada': de_cifrar(mensagem, P)})

# funcao que recebe uma mensagem e retorna a mensagem cifrada com enigma
@app.route('/enigma', methods=['POST'])
def enigma_mensagem():
    data = request.get_json()
    mensagem = data['mensagem']
    P = data['P']
    E = data['E']
    return jsonify({'mensagem_enigma': enigma(mensagem, P, E)})

# funcao que recebe uma mensagem cifrada com enigma e retorna a mensagem original
@app.route('/de-enigma', methods=['POST'])
def de_enigma_mensagem():
    data = request.get_json()
    mensagem = data['mensagem']
    P = data['P']
    E = data['E']
    return jsonify({'mensagem_de_enigma': de_enigma(mensagem, P, E)})


if __name__ == '__main__':
    app.run(debug=True)
