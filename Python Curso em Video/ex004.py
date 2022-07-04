
# Dissecando uma Variável

valor1 = input('Aperte uma tecla')
print(valor1.isnumeric()) #é númerico
print(valor1.isalpha()) #é letra
print(valor1.isupper()) #esta somente com letras maiúsculas
print(valor1.isalnum()) #tem letra e número
print(valor1.isdecimal()) #valor quebrado

a = input('Digite algo:')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É númerico? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())