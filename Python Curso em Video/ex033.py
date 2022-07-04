
# Maior e menor valores

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))

if valor1 < valor2 and valor2 < valor3:
    print("{} é o maior número".format(valor3))
if valor3 < valor1 and valor3 < valor2:
    print("{} é o maior número".format(valor2))

###########################################################

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))