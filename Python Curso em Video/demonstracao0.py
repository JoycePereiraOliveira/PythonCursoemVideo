
# Utilizando Módulos

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))


import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))


import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

#Chamar número aleatório
import random
num = random.random()
print(num)

#Chamar número inteiro, ex: de 1 até 10
import random
num = random.randint(1, 10)
print(num)

#PyPi
import emoji
print(emoji.emojize('Olá mundo! :sunglasses', use_aliase=True))