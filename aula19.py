'''
Peso: Os pesos são parâmetros ajustáveis que representam a força ou importância das conexões entre os 
neurônios. Cada conexão sináptica de entrada para o neurônio possui um peso associado. Durante o treinamento 
da rede neural, os pesos são atualizados de forma a otimizar o desempenho da rede, permitindo que ela aprenda 
a mapear corretamente os inputs para os outputs desejados.

Neurônio: Um neurônio é a unidade fundamental de processamento em uma rede neural. Ele recebe um conjunto de 
inputs, realiza uma operação de soma ponderada desses inputs, aplica uma função de ativação ao resultado e 
produz um output. Cada neurônio pode ter um conjunto de pesos associados aos seus inputs, que são utilizados 
para calcular a soma ponderada.

Bias (viés): O bias é um parâmetro adicional em um neurônio que representa uma medida do quanto o neurônio é 
ativado independentemente dos inputs. O bias permite que o neurônio aprenda a ativar-se mesmo quando os inputs 
são todos iguais a zero. Em outras palavras, ele ajusta o ponto de partida para a ativação do neurônio. O bias 
é somado à soma ponderada dos inputs antes da aplicação da função de ativação.

Função de ativação: A função de ativação é aplicada à soma ponderada dos inputs de um neurônio para determinar 
o seu output. Ela introduz não-linearidade na rede neural, permitindo que ela aprenda relações complexas nos 
dados. Existem diferentes tipos de funções de ativação, como a função sigmoid, função degrau, função ReLU, 
entre outras. Cada função de ativação tem suas características específicas e é escolhida de acordo com o problema 
em questão.

'''

import numpy as np

#Função de ativação
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, num_inputs):
        #Inicializando os pesos aleatóriamente 
        self.weights = np.random.rand(num_inputs)
        #Inicializando os viés aleatoriamente
        self.bias = np.random.rand()

    def forward(self, inputs):
        #Calculando a soma ponderada dos inputs e do bias
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        #Aplicando a função de ativação
        output = sigmoid(weighted_sum)
        return output
    
#Exemplos de input
inputs = np.array([2, 3, 1])

#Criação de um neurônio com 3 entradas
neuron = Neuron(3)

#Calcula o output do neurônio
output = neuron.forward(inputs)

print("Saída:", output)


    
