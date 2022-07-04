
# Sorteando uma ordem na lista

import random
aluno1 = str(input('Digite o nome do aluno: \n'))
aluno2 = str(input('Digite o nome do aluno: \n'))

ordem = [aluno1, aluno2]
random.shuffle(ordem)

print('A ordem é {}'.format(ordem))

#################################################

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
