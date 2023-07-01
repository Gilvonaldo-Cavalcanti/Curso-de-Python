

class MinhaClasse:
    """ Documentação da Classe """

    i = 12345 #Variável Pública
    __a = 1 # Variável Privada

    def f(self):
        return "Hello Wolrd!"
    
    def a(self):
        return "Teste"
    
x = MinhaClasse()

print(x.__doc__)
print(x.f())

class SubClasse(MinhaClasse):
    
    def __init__(self) -> None:
        super().__init__()


sub = SubClasse()

print(sub.i)