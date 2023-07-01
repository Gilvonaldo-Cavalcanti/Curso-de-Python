import pandas as pd
import matplotlib.pyplot as plt

#Carregando os dados do CSV
data = pd.read_csv('dados_vendas.csv')

#Convertendo a coluna 'data' para o tipo datetime
data['data'] = pd.to_datetime(data['data'])

#Vendas nos últimos 12 meses
data['ano_mes'] = data['data'].dt.to_period('M')
vendas_ultimos_12_meses = data.groupby('ano_mes')['quantidade'].sum()

#Convertendo o index em string
vendas_ultimos_12_meses.index = vendas_ultimos_12_meses.index.astype(str)

#Grafico de linhas mostrando a variação das vendas.
plt.plot(vendas_ultimos_12_meses.index, vendas_ultimos_12_meses.values)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Vendas')
plt.title('Variação de Vendas nos Últimos 12 Meses')
plt.xticks(rotation=45)
plt.show()

#Exibindo a resposta.
print("Total de vendas nos últimos 12 meses:", vendas_ultimos_12_meses.sum())
