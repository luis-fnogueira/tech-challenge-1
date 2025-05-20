"""
Production routes for the API.
"""

from flask import Flask, jsonify, request
from scraper import VitiBrasilScraper

def register_production_routes(app: Flask):
    """Register production routes."""
    
    # Initialize the scraper
    scraper = VitiBrasilScraper()
    
    @app.route('/api/production', methods=['GET'])
    def get_production():
        """
        Obtém dados de produção de vinho.
        ---
        tags:
          - Produção
        parameters:
          - name: year
            in: query
            type: integer
            required: false
            description: Ano para obter os dados
        responses:
          200:
            description: Dados de produção obtidos com sucesso
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
                        description: Quantidade produzida
                total:
                  type: number
                  description: Total de produção
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
            data = scraper.get_production_data(year=year)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500 