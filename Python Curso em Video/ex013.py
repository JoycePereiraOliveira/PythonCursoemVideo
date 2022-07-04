
# Reajuste Salarial

salario = float(input('Digite o valor do salário: \n'))

diferenca = salario * 0.15
aumento = diferenca + salario

print('A diferença do valor é de {}, com o aumento o salário fica {} \n'.format(diferenca, aumento))



salario = float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15 /100)
print('Um funcionário que ganhava R${:.0f}, com 15% de aumento, passa a receber R${:.0f}'.format(salario, novo))