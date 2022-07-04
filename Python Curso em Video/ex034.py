
# Aumentos múltiplos

salarioFuncionario = float(input('Digite o salário do funcionário: '))

aumentoSuperior = salarioFuncionario % 0,10
aumentoInferior = salarioFuncionario % 0,15

if salarioFuncionario > 1250.00:
    print('Para salários acima de 1.250,00 o aumento é de 10%. O valor final do seu aumento é {}'.format(aumentoSuperior))
else:
    print('Para salários abaixo de de 1.250,00 o aumento é de 15%. O valor final do seu aumento é {}'.format(aumentoInferior))

#######################################################

salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))