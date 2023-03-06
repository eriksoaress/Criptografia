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
    result = P @ matriz_msg
    return para_string(result)

''' Uma função `de_cifrar(msg : str, P : np.array)` que recupera uma mensagem
cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra.'''
def de_cifrar(msg, P):
    msg = para_one_hot(msg)
    result = np.linalg.inv(P) @ msg
    return para_string(result)

'''Uma função `enigma(msg : str, P : np.array, E : np.array)` que faz a cifra enigma na mensagem de entrada
usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
# def enigma(msg, P, E):
#     result1 = cifrar(msg, P)
#     for indice in (result1.T):
#         if indice != 0:
#             for i in range(indice):
#                 result1 = E @ result1
#     return result1

'''Uma função `de_enigma(msg : str, P : np.array, E : np.array)` que recupera uma mensagem cifrada como enigma
assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
# def de_enigma(msg, P, E):
#     for indice in (msg.T):
#         for i in range(indice):
#             msg = np.linalg.inv(E)

#         msg = np.linalg.inv(P) @ msg


#     result2 = de_cifrar(result1, P)
#     return result2


matriz = np.zeros((26,26), dtype=int)
matriz2 = np.zeros((26,26), dtype=int)


for i in range(26):
    matriz[i, (i+1)%26] = 1
    matriz2[i, (i+2)%26] = 1

teste_enigma = enigma('Olla a todos', matriz, matriz2)
print(teste_enigma)

teste_de_enigma = de_enigma(teste_enigma, matriz, matriz2)
print(teste_de_enigma)