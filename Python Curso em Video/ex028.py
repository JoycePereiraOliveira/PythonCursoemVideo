
# Jogo da Adivinhação

import random
numero = int(input('Adivinhe o número escolhido entre 1 e 5: '))

sorteado = random.randint(1, 5)
print(sorteado)

if numero == sorteado:
    print('Você escolheu {} e o número sorteado foi {}. VOCÊ VENCEU!'.format(numero, sorteado))
else:
    print('Você escolheu {} e o número sorteado foi {}. VOCÊ PERDEU! Tente novamente.'.format(numero, sorteado))

#################################################

from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no [}'.format(computador, jogador))