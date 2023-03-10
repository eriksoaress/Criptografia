# Criptografia Enigma
Este projeto consiste em uma implementação de um cifrador e decifrador Enigma, um famoso dispositivo de criptografia usado pela Alemanha nazista durante a Segunda Guerra Mundial. O objetivo desse dispositivo era codificar mensagens militares e protegê-las contra interceptação e decodificação pelos inimigos.

# Equações Implementadas
Para realizar a criptografia e decodificação com Enigma, foram implementadas as seguintes equações:

## cifrar(msg : str, P : np.array):
Aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. P é a matriz de permutação que realiza a cifra.
- Deve ser realizada uma multiplicação matricial entre a matriz de permutação e a mensagem.


## de_cifrar(msg : str, P : np.array):
Recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. P é a matriz de permutação que realiza a cifra.
- Deve ser realizada uma multiplicação matricial entre a inversa da matriz de permutação e a mensagem, efetuando o caminho inverso da cifra.


## enigma(msg : str, P : np.array, E : np.array):
Faz a cifra Enigma na mensagem de entrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
- Deve ser realizada uma multiplicação matricial entre o P, E0 * E1*...Ei (sendo i o indice correspondente a letra da mensagem) e a mensagem.


## de_enigma(msg : str, P : np.array, E : np.array):
Recupera uma mensagem cifrada como Enigma assumindo que ela foi cifrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
- Deve ser realizada uma multiplicação matricial E0 * E1*...Ei (sendo i o indice correspondente a letra da mensagem), o P, e a mensagem .


# Como Usar
Para utilizar cada uma das funções da biblioteca segue as explições:
- cifrar: Passe a sua mensagem original como método da função, e a sua matriz permutação, sendo essa última opcional, haja vista que já possui uma pre-definida.
- de_cifrar: Passe a sua mensagem cifrada como método da função, e a matriz permutação, sendo essa última opcional, haja vista que já possui uma pre-definida.
- enigma: Passe a sua mensagem original como método da função, a matriz permutação, e a matriz permutação auxiliar, sendo as duas últimas opcionais, haja vista que elas estão pre-definidas.
- de_enigma: Passe o seu enigma como método da função, a matriz permutação, e a matriz permutação auxiliar, sendo as duas últimas opcionais, haja vista que elas estão pre-definidas.


# Como Rodar o demo.py
Primeiramente, verifique se você está na pasta criptografia, após isso, abra o seu terminal e execute o seguinte comando: python demo.py
Será exibido em seu terminal alguns testes de cada uma das funções que foram implementadas.