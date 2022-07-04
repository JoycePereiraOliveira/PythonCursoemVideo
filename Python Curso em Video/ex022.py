
# Analisador de Textos

nomePessoa = str(input('Digite seu nome completo: \n')).strip()
maiuscula = nomePessoa.upper()
print(maiuscula)


minusculo = nomePessoa.lower()
print(minusculo)


totalLetras = len(nomePessoa)

totalLetras = nomePessoa.strip()
totalLetras = len(nomePessoa)
print(totalLetras)

letrasPrimeiroNome = nomePessoa.split()
print(len(letrasPrimeiroNome[0]))

#--------------------------------------#

nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nomePessoa.upper()))
print('Seu nome em minúsculas é {}'.format(nomePessoa.upper()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele te {} letras'.format(separa[0], len(separa[0])))
