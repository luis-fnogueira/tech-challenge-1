"""
Export routes for the API.
"""

from flask import Flask, jsonify, request
from scraper import VitiBrasilScraper

def register_export_routes(app: Flask):
    """Register export routes."""
    
    # Initialize the scraper
    scraper = VitiBrasilScraper()
    
    @app.route('/api/export', methods=['GET'])
    def get_export():
        """
        Obtém dados de exportação para todas as categorias de produtos vitivinícolas.
        ---
        tags:
          - Exportação
        parameters:
          - name: year
            in: query
            type: integer
            required: false
            description: Ano para obter os dados
        responses:
          200:
            description: Dados de exportação obtidos com sucesso
            schema:
              type: object
              properties:
                year:
                  type: integer
                  description: Ano dos dados
                categories:
                  type: object
                  description: Dados de exportação para cada categoria
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
            data = scraper.get_all_export_data(year=year)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/export/<category>', methods=['GET'])
    def get_export_by_category(category):
        """
        Obtém dados de exportação para uma categoria específica de produtos vitivinícolas.
        ---
        tags:
          - Exportação
        parameters:
          - name: category
            in: path
            type: string
            required: true
            description: Categoria de exportação (vinhos_mesa, espumantes, uvas_frescas, suco_uva)
            enum: [vinhos_mesa, espumantes, uvas_frescas, suco_uva]
          - name: year
            in: query
            type: integer
            required: false
            description: Ano para obter os dados
        responses:
          200:
            description: Dados de exportação obtidos com sucesso
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
                countries:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: Nome do país
                      quantity:
                        type: number
                        description: Quantidade exportada
                      value:
                        type: number
                        description: Valor da exportação
                total:
                  type: object
                  properties:
                    quantity:
                      type: number
                      description: Total de quantidade exportada
                    value:
                      type: number
                      description: Total de valor exportado
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
            data = scraper.get_export_data(category=category, year=year)
            return jsonify(data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500 