# Leitura e Escrita de Arquivos em Python

arquivo = open("Exemplo.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

arquivo = open("Exemplo.txt", "r")
conteudo = arquivo.read()

print(conteudo)

# Tratamento de Exceções em Python

'''
try: 
    código que pode gerar uma exceção
except tipoDeExceção:
    código para lidar com a exceção
'''

def divisor():
    x = 1/0

try:
    divisor()
except ZeroDivisionError as err:
    print("Deu erro =>", err)


