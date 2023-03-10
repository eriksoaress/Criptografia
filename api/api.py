from flask import Flask,  jsonify, request
from main import enigma, de_enigma
import numpy as np
app = Flask(__name__)

# funcao que recebe uma mensagem e retorna a mensagem cifrada com enigma
@app.route('/enigma', methods=['POST'])
def enigma_mensagem():
    data = request.get_json()
    mensagem = data['mensagem']
    return jsonify({'mensagem_enigma': enigma(mensagem)})

# funcao que recebe uma mensagem cifrada com enigma e retorna a mensagem original
@app.route('/de-enigma', methods=['POST'])
def de_enigma_mensagem():
    data = request.get_json()
    mensagem = data['mensagem']
    return jsonify({'mensagem_de_enigma': de_enigma(mensagem)})


if __name__ == '__main__':
    app.run(debug=True)
