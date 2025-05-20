"""
Processing routes for the API.
"""

from flask import Flask, jsonify, request
from scraper import VitiBrasilScraper

def register_processing_routes(app: Flask):
    """Register processing routes."""
    
    # Initialize the scraper
    scraper = VitiBrasilScraper()
    
    @app.route('/api/processing', methods=['GET'])
    def get_processing():
        """
        Obtém dados de processamento de uvas para todas as categorias.
        ---
        tags:
          - Processamento
        parameters:
          - name: year
            in: query
            type: integer
            required: false
            description: Ano para obter os dados
        responses:
          200:
            description: Dados de processamento obtidos com sucesso
            schema:
              type: object
              properties:
                year:
                  type: integer
                  description: Ano dos dados
                categories:
                  type: object
                  description: Dados de processamento para cada categoria
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
            data = scraper.get_all_processing_data(year=year)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/processing/<category>', methods=['GET'])
    def get_processing_by_category(category):
        """
        Obtém dados de processamento de uvas para uma categoria específica.
        ---
        tags:
          - Processamento
        parameters:
          - name: category
            in: path
            type: string
            required: true
            description: Categoria de uva (viniferas, americanas, mesa, sem_classificacao)
            enum: [viniferas, americanas, mesa, sem_classificacao]
          - name: year
            in: query
            type: integer
            required: false
            description: Ano para obter os dados
        responses:
          200:
            description: Dados de processamento obtidos com sucesso
            schema:
              type: object
              properties:
                year:
                  type: integer
                  description: Ano dos dados
                title:
                  type: string
                  description: Título dos dados
                category:
                  type: string
                  description: Nome da categoria
                varieties:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: Nome da variedade
                      quantity:
                        type: number
                        description: Quantidade processada
                      subvarieties:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                              description: Nome da subvariedade
                            quantity:
                              type: number
                              description: Quantidade processada
                total:
                  type: number
                  description: Total de processamento
          400:
            description: Categoria inválida
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Mensagem de erro
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
            data = scraper.get_processing_data(category=category, year=year)
            return jsonify(data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500 