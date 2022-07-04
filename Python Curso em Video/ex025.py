
# Procurando uma string dentro de outra

nomePessoa = str(input('Digite seu nome completo: \n')).strip()
print(nomePessoa[:5].upper == 'SILVA')

#################################

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.lower()))