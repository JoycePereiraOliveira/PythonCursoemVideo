
# Separando digitos de um número

valor = int(input('Digite um número: \n'))
numero = str(valor)

print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))

#---------------------------------------#
valor = int(input('Digite um número: \n'))
unidade = numero // 1 % 10

print('Unidade: {}'.format(numero))
print('Dezena: {}'.format(numero))
print('Centena: {}'.format(numero))
print('Milhar: {}'.format(numero))
