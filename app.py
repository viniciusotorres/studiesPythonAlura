import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()

    # Verificar se a resposta é uma lista
    if isinstance(dados_json, list):  #Verifica se a variável dados_json é uma lista
        dados_restaurante = {} #Cria um dicionário vazio
        for restaurante in dados_json: #Percorre a lista de restaurantes
            nome_restaurante = restaurante['Company'] #Pega o nome do restaurante
            if nome_restaurante not in dados_restaurante: #Verifica se o nome do restaurante não está no dicionário
                dados_restaurante[nome_restaurante] = [] #Cria uma lista vazia para o restaurante

            dados_restaurante[nome_restaurante].append({ #Adiciona um dicionário com os dados do restaurante na lista
                "item": restaurante['Item'],    #Adiciona o item
                "price": restaurante['price'], #Adiciona o preço
                "description": restaurante['description'] #Adiciona a descrição
            })
    else:
        print('Erro: A resposta da API não é uma lista.') #Se a resposta não for uma lista, exibe um erro
else:
    print('Erro ao acessar a API') # Se a resposta não for 200, exibe um erro
    print(response.status_code) #Exibe o código de status da resposta

for nome_restaurante, dados in dados_restaurante.items(): #Percorre o dicionário de restaurantes
    nome_do_arquivo = f'{nome_restaurante}.json' #Cria o nome do arquivo
    with open(nome_do_arquivo, 'w') as arquivo: #Abre o arquivo para escrita
        json.dump(dados, arquivo, indent=4) #Escreve os dados no arquivo

