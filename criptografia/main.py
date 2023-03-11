import numpy as np
from flask import jsonify

alfabeto =[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&','*','(',')','-','_','+','=','?']

matriz = np.zeros((len(alfabeto),len(alfabeto)), dtype=int)
matriz2 = np.zeros((len(alfabeto),len(alfabeto)), dtype=int)
for i in range(len(alfabeto)):
    matriz[i, (i+1)%len(alfabeto)] = 1
    matriz2[i, (i+2)%len(alfabeto)] = 1


def valida_mensagem(msg):
    if msg == '':
            raise ValueError
    return True


'''Uma função `para_one_hot(msg : str)` para codificar mensagens como uma matriz usando one-hot encoding'''
def para_one_hot(msg):
    try:
        
        if valida_mensagem(msg):
            matriz = np.zeros([len(alfabeto),len(msg)])
            msg = msg.lower()
            for j, letra in enumerate(msg):
                if letra in alfabeto:
                    i = alfabeto.index(letra)
                    matriz[i][j] = 1
                else:
                    if letra.isspace():
                        for coluna in range(len(alfabeto)):
                            matriz[coluna][j] = 0
                    else:
                        for coluna in range(len(alfabeto)):
                            matriz[coluna][j] = 1
        
    except:
        return {"erro": "Mensagem inválida, coloque uma string não vazia"}
    return matriz




'''Uma função `para_string(M : np.array)` para converter mensagens da representação one-hot encoding para uma string legível'''
def para_string(M):
    msg = ''
    try:
        for coluna in M.T:
            quantidade = 0
            for i, elemento in enumerate(coluna):
                if elemento == 1:
                    quantidade+=1
                    indice = i
            if quantidade > 1:
                msg += '?'
            elif quantidade == 1:
                msg += alfabeto[indice]
            else:
                msg += ' '
    except:
        return {"erro": "Mensagem inválida, coloque uma matriz (np.array)"}
    return msg



'''Uma função `cifrar(msg : str, P : np.array)` que aplica uma cifra simples
em uma mensagem recebida como entrada e retorna a mensagem cifrada. `P` é a
matriz de permutação que realiza a cifra.'''
def cifrar(msg, P=matriz):
    try:
        if valida_mensagem(msg):
            matriz_msg = para_one_hot(msg)
            result = P @ matriz_msg
            return para_string(result)
        
    except:
        return {"erro":"Não há mensagem, ou a matriz P não é válida" }

''' Uma função `de_cifrar(msg : str, P : np.array)` que recupera uma mensagem
cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra.'''
def de_cifrar(msg, P=matriz):
    try:
        if  valida_mensagem(msg):
            msg = para_one_hot(msg)
            result = np.linalg.inv(P) @ msg
            return para_string(result)
    except:
        return {"erro": "Não há mensagem, ou a matriz P não é válida"}

'''Uma função `enigma(msg : str, P : np.array, E : np.array)` que faz a cifra enigma na mensagem de entrada
usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
def enigma(msg, P=matriz, E=matriz2):
    
    try:
        if valida_mensagem(msg):
            matriz = ''
            result1 = P@para_one_hot(msg)
            for indice, coluna in enumerate(result1.T):
                if indice != 0:
                    coluna = np.array([[x] for x in coluna])
                    for i in range(indice):
                        coluna = E @ coluna
                    matriz = np.hstack((matriz, coluna))
                else:
                    matriz = np.array([[x] for x in coluna])
    except:
        return {'erro': 'Não há mensagem, ou a matriz P ou E não é válida'}
    return para_string(matriz)

'''Uma função `de_enigma(msg : str, P : np.array, E : np.array)` que recupera uma mensagem cifrada como enigma
assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
def de_enigma(msg, P=matriz, E=matriz2):
      
    try:
        if valida_mensagem(msg):
            matriz = ''
            result1 = para_one_hot(msg)
            for indice, coluna in enumerate(result1.T):
                if indice != 0:
                    coluna = np.array([[x] for x in coluna])
                    for i in range(indice):
                        coluna = np.linalg.inv(E) @ coluna
                    coluna = np.linalg.inv(P) @ coluna
                    matriz = np.hstack((matriz, coluna))
                else:
                    matriz = np.array([[x] for x in coluna])
                    matriz = np.linalg.inv(P) @ matriz
    except:
        return {"erro":"Não há mensagem, ou a matriz P ou E não é válida"}
    return para_string(matriz)


