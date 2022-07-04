
# Seno, Cosseno e Tangente

import math
angulo = float(input('Informe um valor para o ângulo: \n'))

seno = math.sin(math.radians(angulo))
print('O valor do seno é {}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O valor do cosseno é {}'.format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O valor da tangente é {}'.format(angulo, tangente))

############################################################

from math import radians, sin, cos, tan
angulo = float(input('Informe um valor para o ângulo: \n'))

seno = sin(radians(angulo))
print('O valor do seno é {}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O valor do cosseno é {}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O valor da tangente é {}'.format(angulo, tangente))