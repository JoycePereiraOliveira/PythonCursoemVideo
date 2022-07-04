
# Aluguel de Carros

km = float(input('Quanto km foi percorrido pelo carro alugado? \n'))
dia = int(input('Por quantos dias ele foi alugado? \n'))

total = (60 * dia) + (km * 0.15)

print('Foi alugado por {} dias, percorreu {}km, portanto o valor a ser pago é de: R${}'.format(dia, km, total))



dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))