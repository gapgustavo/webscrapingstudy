import requests
import re
from bs4 import BeautifulSoup
import yaml

# Fazer requisição GET à página
url = 'https://www.w3schools.io/file/yaml-sample-example/'
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrair o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrar o exemplo de arquivo YAML
    yaml_example = soup.find('pre')
    if yaml_example:
        # Extrair o texto do exemplo
        yaml_text = yaml_example.text
        # Utilizar REGEX para extrair os comentários contidos no exemplo
        comments = re.findall(r'#\s.*', yaml_text)
        # Imprimir os comentários na tela
        print('Comentários encontrados:')
        for comment in comments:
            print(comment)
        
        # Escrever o exemplo de arquivo YAML em um novo arquivo
        with open('example.yaml', 'w') as file:
            file.write(str(comments))
        print('Arquivo example.yaml criado com sucesso!')
    else:
        print('Exemplo de arquivo YAML não encontrado na página.')
else:
    print('Falha na requisição à página. Código de status:', response.status_code)
