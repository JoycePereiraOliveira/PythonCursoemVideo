
# Primeiro e último nome de uma pessoa

nomeCompleto= str(input('Digite seu nome completo: ')).strip()
nome = nomeCompleto.split()
print(nome[0])

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))