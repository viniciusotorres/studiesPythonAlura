from flask import Flask, request, jsonify
import requests
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/restaurantes/', methods=['GET'])
def get_restaurantes():
    """
    Endpoint para ver os cardápios dos restaurantes
    ---
    parameters:
      - name: restaurante
        in: query
        type: string
        required: false
        description: Nome do restaurante
    responses:
      200:
        description: Lista de cardápios dos restaurantes
        schema:
          type: object
          properties:
            Restaurante:
              type: string
              description: Nome do restaurante
            Cardapio:
              type: array
              items:
                type: object
                properties:
                  item:
                    type: string
                    description: Nome do item
                  price:
                    type: string
                    description: Preço do item
                  description:
                    type: string
                    description: Descrição do item
      400:
        description: Erro na requisição
    """
    restaurante = request.args.get('restaurante')
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return jsonify({'Dados': dados_json})

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return jsonify({'Restaurante': restaurante, 'Cardapio': dados_restaurante})
    else:
        return jsonify({'Erro': f'{response.status_code} - {response.text}'})

if __name__ == '__main__':
    app.run(debug=True)