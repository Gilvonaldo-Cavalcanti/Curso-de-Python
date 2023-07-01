from django.shortcuts import render
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import os

def index(request):
    if request.method == 'POST':
        try:
            url = request.POST['url']
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # Contagem das tags
            tags = soup.find_all()
            tags_count = len(tags)

            # Contagem de tags únicas
            unique_tags = set(tag.name for tag in tags)
            unique_tags_count = len(unique_tags)

            # Contagem das tags mais comuns
            tags_frequency = pd.Series(tag.name for tag in tags)
            top_tags = tags_frequency.value_counts().head(5)

            # Contagem das classes mais comuns
            classes = [tag.get('class') for tag in tags if tag.get('class')]
            classes_frequency = pd.Series([c for cl in classes for c in cl])
            top_classes = classes_frequency.value_counts().head(5)
            
            #Gráfico do Matplotlib 
            grafico = grafico_estatistico(classes_frequency=classes_frequency, 
                                                            tags_count=tags_count, 
                                                            unique_tags_count=unique_tags_count)


            return render(request, 'scraper/index.html', 
                        {'tags_count': tags_count, 'unique_tags_count': unique_tags_count, 
                        'top_tags': top_tags, 'top_classes': top_classes, 
                        'graph_path': grafico})
        except:
            return render(request, 'scraper/index.html')

    else:
        return render(request, 'scraper/index.html')
    

def grafico_estatistico(classes_frequency, tags_count, unique_tags_count):
    class1 = classes_frequency.value_counts().head(1).quantile()
    class2 = classes_frequency.value_counts().head(2).quantile()
    class3 = classes_frequency.value_counts().head(3).quantile()
            
    # Dados para o gráfico
    data = {
            'Tag': ['Quant. Tags', 'Tags Unic.', classes_frequency[1], classes_frequency[2], classes_frequency[3],],
            'Quantidade': [tags_count, unique_tags_count, class1, class2, class3]
        }
        
    # Criação do DataFrame a partir dos dados
    df = pd.DataFrame(data)
        
    # Configuração do tamanho do gráfico
    plt.figure(figsize=(8, 6))
        
    # Plotagem do gráfico de barras
    plt.bar(df['Tag'], df['Quantidade'])
        
    # Configuração dos rótulos e título do gráfico
    plt.xlabel('Tag')
    plt.ylabel('Quantidade')
    plt.title('Estatísticas das Tags')
        
    # Caminho para salvar o gráfico
    graph_path = os.path.join('images', 'graph.png')
        
    # Salvar o gráfico no diretório static/images
    plt.savefig(os.path.join('scraper', 'static', graph_path))

    return graph_path