
#Exemplo1
carro.siga()

if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()

elif carro.direita(): #Elif - Else if
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()

else:
    carro.siga()
    carro.para()

carro.para()

#Exemplo2
nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))