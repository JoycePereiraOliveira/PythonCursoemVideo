
# Primeira e última ocorrência de uma string

frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A apareceu na posição {}'.format(frase.count('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))