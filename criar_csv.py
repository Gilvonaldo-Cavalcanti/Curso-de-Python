import pandas as pd

#Dados das vendas
data  = {
    'data': ['2022-01-01', '2022-01-05', '2022-02-10', '2022-03-15', '2022-03-20'],
    'produto' : ['A', 'B', 'C', 'A', 'B'],
    'categoria' : ['Eltronicos', 'Moda', 'Eltronicos', 'Eltronicos', 'Moda'],
    'quantidade' : [10,5,8,12,7],
    'valor_total': [100.0, 50.0, 80.0, 120.0, 70.0]
}

#Criando o DataFrame
df = pd.DataFrame(data)

#Salvando os dados em um arquivo CSV
df.to_csv('dados_vendas.csv', index=False)