# Criptografia Enigma
Este projeto consiste em uma implementação de um cifrador e decifrador Enigma, um famoso dispositivo de criptografia usado pela Alemanha nazista durante a Segunda Guerra Mundial. O objetivo desse dispositivo era codificar mensagens militares e protegê-las contra interceptação e decodificação pelos inimigos.

Equações Implementadas
Para realizar a criptografia e decodificação com Enigma, foram implementadas as seguintes equações:

cifrar(msg : str, P : np.array): aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. P é a matriz de permutação que realiza a cifra.
de_cifrar(msg : str, P : np.array): recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. P é a matriz de permutação que realiza a cifra.
enigma(msg : str, P : np.array, E : np.array): faz a cifra Enigma na mensagem de entrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
de_enigma(msg : str, P : np.array, E : np.array): recupera uma mensagem cifrada como Enigma assumindo que ela foi cifrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação
