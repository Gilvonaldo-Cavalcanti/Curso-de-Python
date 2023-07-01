# Definição de Funções

def teste():
    print("Função Teste")

teste()

# Definindo Parâmetros

def teste1(nome):
    print(nome)

teste1("José Joaquim")

def teste2(nome="Nome Padrão"):
    print(nome)

teste2()
teste2("Maria Antônia")

def teste3(*nome, **cidades):
    print(nome)
    print(cidades)

teste3("José", "Maria", "João", "Joaquim", paraiba="Monteiro", pernambuco="Sertânia")

# Lambda

# lambada {argumentos} : {expressão}

soma = lambda x, y : x + y

print(soma(2,3))

# Parâmetros especiais

# / e * 


def nome_funcao(pos1, pos2, /, pos_ou_nomeado, *, nom1, nom2):
    pass

