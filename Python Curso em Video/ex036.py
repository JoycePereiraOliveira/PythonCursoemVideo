valorCasa = float(input('Digite o valor do imóvel:'))
salaraioComprador = float(input('Digite a renda do comprador do imóvel:'))
tempoParaQuitar = int(input('Digite a extimativa de tempo que levará para quitar este imóvel:'))


parcela = valorCasa/ tempoParaQuitar
autorizado = parcela

print('O valor a ser pago até quitar o imóvel é de: '.format(parcela))

if parcela>0.30():
    print('Sua renda não condiz com o valor das parcelas deste imóvel.')
else:


