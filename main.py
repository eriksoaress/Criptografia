import numpy as np


alfabeto =[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


'''Uma função `para_one_hot(msg : str)` para codificar mensagens como uma matriz usando one-hot encoding'''
def para_one_hot(msg):
    matriz = np.zeros([26,len(msg)])
    msg = msg.lower()
    for j, letra in enumerate(msg):
        if letra in alfabeto:
            i = alfabeto.index(letra)
            matriz[i][j] = 1
        else:
            if letra.isspace():
                for linha in range(26):
                    matriz[linha][j] = 0
            else:
                for linha in range(26):
                    matriz[linha][j] = 1
    return matriz




'''Uma função `para_string(M : np.array)` para converter mensagens da representação one-hot encoding para uma string legível'''
def para_string(M):
    msg = ''
    for linha in M.T:
        quantidade = 0
        for i, elemento in enumerate(linha):
            if elemento == 1:
                quantidade+=1
                indice = i
        if quantidade > 1:
            msg += '?'
        elif quantidade == 1:
            msg += alfabeto[indice]
        else:
            msg += ' '
    return msg



'''Uma função `cifrar(msg : str, P : np.array)` que aplica uma cifra simples
em uma mensagem recebida como entrada e retorna a mensagem cifrada. `P` é a
matriz de permutação que realiza a cifra.'''
def cifrar(msg, P):
    matriz_msg = para_one_hot(msg)
    return P @ matriz_msg

''' Uma função `de_cifrar(msg : str, P : np.array)` que recupera uma mensagem
cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra.'''
def de_cifrar(msg, P):
    return np.linalg.inv(P) @ msg

'''Uma função `enigma(msg : str, P : np.array, E : np.array)` que faz a cifra enigma na mensagem de entrada
usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
def enigma(msg, P, E):
    pass

'''Uma função `de_enigma(msg : str, P : np.array, E : np.array)` que recupera uma mensagem cifrada como enigma
assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
def de_enigma(msg, P, E):
    pass