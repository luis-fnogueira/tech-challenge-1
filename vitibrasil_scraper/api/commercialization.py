"""
Commercialization routes for the API.
"""

from flask import Flask, jsonify, request
from scraper import VitiBrasilScraper

def register_commercialization_routes(app: Flask):
    """Register commercialization routes."""
    
    # Initialize the scraper
    scraper = VitiBrasilScraper()
    
    @app.route('/api/commercialization', methods=['GET'])
    def get_commercialization():
        """
        Obtém dados de comercialização de vinhos e derivados.
        ---
        tags:
          - Comercialização
        parameters:
          - name: year
            in: query
            type: integer
            required: false
            description: Ano para obter os dados
        responses:
          200:
            description: Dados de comercialização obtidos com sucesso
            schema:
              type: object
              properties:
                year:
                  type: integer
                  description: Ano dos dados
                products:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: Nome do produto
                      quantity:
                        type: number
                        description: Quantidade comercializada
                total:
                  type: number
                  description: Total de comercialização
          500:
            description: Erro interno do servidor
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Mensagem de erro
        """
        year = request.args.get('year')
        
        try:
            if year:
                year = int(year)
            data = scraper.get_commercialization_data(year=year)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500 