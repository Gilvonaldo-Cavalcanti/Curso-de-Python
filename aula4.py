#EStrutura de Condição

a = 10

if (a < 5):
    print("A é menor que 5")
elif (a > 5):
    print("A é maior que 5")
else:
    print("A é igual a 5")

#Loops

condicao = True

while (condicao):
    print("=======================")
    condicao = input("Digite P para sair")
    if (condicao == "P"):
        condicao = False
    else:
        condicao = True
    
lista = ["Python", "Java", "Go"]

for i in lista:
    print(i)

for i in range(4):
    print(i)


for i in "José Silva":
    print(i)