import re

# Manipulação de Strings

var1 = '{0}, {1}, {2}'.format('A', 'B', 'C')

print(var1)

var2 = 'Cordenadas: {latitude}, {longitude}'.format(latitude='12', longitude='-115')

print(var2)

# Expressões Regulares

def vericador_email(email):
    padrao = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email)