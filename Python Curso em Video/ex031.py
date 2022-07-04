
# Custo da Viagem

distanciaViagem = float(input("Qual a distância desta viagem? "))

precoViagem50 = distanciaViagem * 0,50
precoViagem45 = distanciaViagem * 0,45

if distanciaViagem == 200:
    print("Para viagens abaixo de 200km é cobrado 0,50 por km. Valor da sua viagem é de {}".format(precoViagem50))
else:
    print("Para viagens mais longas é cobrado 0,45 por km. O valor da sua viagem é de {}".format(precoViagem45))

#########################################################3
distancia = float(input('Qual é a distância da sa viagem?'))
print('Você está prestes a começar uma viagem de {}km.')
if distancia <= 200:
    preco = distancia  * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua viagem será de R${:.2f}'.format(preco))

#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45