'''Uma função `para_one_hot(msg : str)` para codificar mensagens como uma matriz usando one-hot encoding'''
def para_one_hot(msg):
    alfabeto =[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pass

'''Uma função `para_string(M : np.array)` para converter mensagens da representação one-hot encoding para uma string legível'''
def para_string(M):
    pass

'''Uma função `cifrar(msg : str, P : np.array)` que aplica uma cifra simples
em uma mensagem recebida como entrada e retorna a mensagem cifrada. `P` é a
matriz de permutação que realiza a cifra.'''
def cifrar(msg, P):
    pass

''' Uma função `de_cifrar(msg : str, P : np.array)` que recupera uma mensagem
cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra.'''
def de_cifrar(msg, P):
    pass

'''Uma função `enigma(msg : str, P : np.array, E : np.array)` que faz a cifra enigma na mensagem de entrada
usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
def enigma(msg, P, E):
    pass

'''Uma função `de_enigma(msg : str, P : np.array, E : np.array)` que recupera uma mensagem cifrada como enigma
assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação.'''
def de_enigma(msg, P, E):
    pass