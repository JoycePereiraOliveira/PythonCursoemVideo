
# Analisando Triângulo

reta1 = int(input("Digita o valor da primeira reta: "))
reta2 = int(input("Digite o valor da segunda reta: "))
reta3 = int(input("Digite o valor da terceira reta: "))

triangulo = reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2

if triangulo:
    print("O triângulo pode ser formado")
else:
    print("O triângulo não pode ser formado")

#########################################################
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
