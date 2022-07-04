
# Calculando Descontos

produto = float(input('Qual o valor deste produto? \n'))

desconto = produto * 0.05
descontado = produto - desconto

print('O valor deste produto com 5% de desconto é de R${}'.format(descontado))



preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 /100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preco, novo))

#preco - 5%