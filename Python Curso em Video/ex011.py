
# Pintando Parede

largura = float(input('Qual a largura desta parede em metros? \n'))
altura = float(input('Qual a altura desta parede em metros? \n'))

area = largura * altura
tinta = area / 2

print('A área desta parede em metros é de {} e precisará de {} de tinta'.format(area, tinta))



larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m² '.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))