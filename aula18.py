import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Dados de exemplo: preço das casas em milhares (variável dependente) e tamnaho em metro quadrados (variável independente)
preco_casas = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
tamanho_casas = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])

#Dividir os dados em conjunto de treinamento e teste
tamanho_casas = tamanho_casas.reshape(-1, 1)#É necessário redimensionar para uma matriz coluna
X_train, X_test, y_train, y_test = train_test_split(tamanho_casas, preco_casas, test_size=0.2, random_state=42)

#Criando uma instância do modelo de Regressão Linear
model = LinearRegression()

#Treinar o modelo usando os dados de treinamento
model.fit(X_train, y_train)

#Fazer previsoes nos dados de teste
previsaoes = model.predict(X_test)

#Calcular o erro médio quadrático
mse = mean_squared_error(y_test, previsaoes)

#Exibir os resultados
print("Dados de teste:", X_test.flatten())
print("Preços reais das casas:", y_test)
print("Previsões de preços das casas:", previsaoes)
print("Erro médio quadrático da regressão:", mse)
