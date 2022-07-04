
# Catetos e Hipotenusa

catetoOposto = float(input('Informe o comprimento do Cateto Oposto: \n'))
catetoAdjacente = float(input('Informe o comprimento do Cateto Adjacente \n'))

hipotenusa = catetoOposto + catetoAdjacente ** (1/2)

print('O valor da Hipotenusa é {}'.format(hipotenusa))

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))

import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))