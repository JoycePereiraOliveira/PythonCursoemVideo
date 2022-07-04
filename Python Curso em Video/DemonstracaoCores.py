
# Cores no Terminal

# \033[style; text; backgroundm

# \033[0;33;44m
# 0 None - sem estilo;
# 1 Bold - negrito;
# 4 Underline - sublinhar;
# e 7 Negative - inverter as configurações;
# Cores Text - 30 ao 37;
# Cores Back - 20 ao 47;

# TESTE - \033[0;30;41m
# TESTE - \033[4;33;44m
# TESTE - \033[1;35;43m
# TESTE - \033[30;42m
# TESTE -\033[m
# TESTE - \033[7;30m

print('\033[1;31;43mOlá, Mundo!\033[m')

print('\033[4;30;45mOlá, Mundo!\033[m')

print('\033[30mOlá, Mundo!\033[m')

print('\033[7;30mOlá, Mundo!\033[m')

print('\033[0;33;44mOlá, Mundo!\033[m')

print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m()\033[m e \033[31m()\033[m!!!'.format(a, b))

print('Os valores são \033[32;44m()\033[m e \033[31;44m()\033[m!!!'.format(a, b))

nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['limpa'], nome, cores['limpa']))

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))




