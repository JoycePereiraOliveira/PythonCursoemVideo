anoNascimento = int(input('Informe seu ano de nascimento:'))

if anoNascimento == 45:
    print('Você condiz com a idade para alistamento (limite de idade: 45 anos)')
elif anoNascimento == 18:
    print('Você tem seis meses apartir dos 18 anos para se alistar')
elif anoNascimento <18 or anoNascimento >45:
    print('Você não pode se alistar (idade minima: 18 anos), (limite de idade: 45 anos).')
