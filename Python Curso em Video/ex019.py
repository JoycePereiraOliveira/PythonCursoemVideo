
# Sorteando um item na lista

import random
aluno1 = str(input('Digite o nome de um aluno: \n'))
aluno2 = str(input('Digite o nome de um aluno: \n'))

sorteio = [aluno1, aluno2]

sorteado = random.choice(sorteio)
print('O aluno sorteado foi {}'.format(sorteado))

#####################################################

from random import choice
aluno1 = str(input('Digite o nome de um aluno: \n'))
aluno2 = str(input('Digite o nome de um aluno: \n'))

sorteio = [aluno1, aluno2]

sorteado = choice(sorteio)
print('O aluno sorteado foi {}'.format(sorteado))