import numpy as np
import matplotlib.pyplot as plt

# data from United Nations World Population Prospects (Revision 2019)
# https://population.un.org/wpp/, license: CC BY 3.0 IGO
ano = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
população_por_continente = {
    'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],
    'americas': [340, 425, 519, 619, 727, 840, 943, 1006],
    'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
    'europa': [220, 253, 276, 295, 310, 303, 294, 293],
    'oceania': [12, 15, 19, 22, 26, 31, 36, 39],
}

fig, ax = plt.subplots()
ax.stackplot(ano, população_por_continente.values(),
             labels=população_por_continente.keys(), alpha=0.8)
ax.legend(loc='upper left')
ax.set_title('População Mundial')
ax.set_xlabel('Ano')
ax.set_ylabel('Número de pessoas (milhões)')

plt.show()