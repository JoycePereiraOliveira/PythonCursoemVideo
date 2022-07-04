
# Radar eletrônico

velocidadeCarro = int(input("Digite a velocidade em que o carro está:"))

multa = (velocidadeCarro-80) * 7

if velocidadeCarro <=80:
    print("Você está dentro do limite.")
else:
    print("Você ultrapassou o limite, o valor da sua multa é {}".format(multa))

############################################

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')