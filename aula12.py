import pandas as pd

times = {'Flamengo': ['Libertadores', 'Mundial', '  Brasileiro', 'Copa do Brasil'],
         'Palmeiras': ['Libertadores', 'Campeonato Estadual', 'Brasileirão', 'Copa do Brasil'],
         'Sport': ['Campeonato Estadual', 'Série B', 'Copa do Nordeste', 'Camp. Regional']}

#pd.read_excel("/home/...tabela.xlsc")

tabela = pd.DataFrame(times)

print(tabela.describe())