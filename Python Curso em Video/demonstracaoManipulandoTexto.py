
# Manipulando Textos

frase = ('Curso em Video Python')

frase[9] #Mostra letra do campo 9

frase[9:13] #Mostra sempre o número anterior ao escolhido (vai até o 12)

frase[9:21:2] #9 Começa | 21 Termina | Pula (de 2 em 2)

frase[:5] #Inicia do caractere zero e vai até a letra 5 (no caso ignoraria o 5 e mostraria até o 4)

frase[15:] #Começa no 15. Não foi indicado até onde vai, então iria até o final

frase[9::3] #Começa no 9 pulando, vai até o final, pulando de 3 em 3

#####################################################################

#ANÁLISE DE UMA STRING

len(frase) #Mostrar comprimento da frase

frase.count('o') #Contar quantas vezes aparece a letra

frase.count('o', 0, 13) #Contagem já com o fatiamento

frase.find('deo') #Quantas vezes encontrou DEO na frase, mostrando a posição que se encontra

frase.find('Android') #Quando não possui a string o programa te retorna -1, significa que não foi encontrado
'Curso' in frase #Não mostra a posição

#####################################################################

#TRANSFORMAÇÃO

frase.replace('Python', 'Android') #Replace = encontrar, procurar. Irá substituir um pelo outro, substitui de uma forma secundária

frase.upper() #Upper = para cima. Todas letras que não são maiúsculas passam a ser

frase.lower() #Lower = para baixo. Todas letras que não são minúsculas passam a ser

frase.capitalize() #Altera tudo para minúsculo, menos a primeira letra

frase.title() #Analisa quantas palavras tem a string. Altera a primeir letra de cada palavra para maiúsculo

frase.strip() #Remove todo espaço inútil, começo e final

frase.rstrip() #Remove todo espaço lado direito

frase.lstrip() #Remove todo espaço lado esquerdo

#####################################################################

#DIVISÃO

frase.split() #Onde estiver espaço ele cria uma divisão em uma lista, cada um terá uma numeração. Cada divisão feita a numeração será 0

#####################################################################

#JUNÇÃO

'-'.join(frase) #Junta todos os elementos de frase, usando o separador escolhido (exemplo-exemplo)































