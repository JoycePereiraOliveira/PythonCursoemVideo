
# Conversor de Moedas

real = float(input('Quanto você tem em sua carteira? \n'))
print('Você tem {} em sua carteira'.format(real))

dolarValeEmReal = 5.28
compraDolar = real / 5.28

print('O dólar vale {} em reais'.format(dolarValeEmReal))
print('Você pode comprar {:.0f} dólares'.format(compraDolar))


real = float(input('Quanto dinheiro você tem na carteira?'))
dolar = real / 3.27
print('Com R${} você pode comprar US${}'.format(real, dolar))