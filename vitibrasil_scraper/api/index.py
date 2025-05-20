"""
Rota de índice para a API.
"""

from flask import Flask, jsonify
from flasgger import Swagger

from .production import register_production_routes
from .processing import register_processing_routes
from .commercialization import register_commercialization_routes
from .imports import register_import_routes
from .exports import register_export_routes

# Create Flask app
app = Flask(__name__)

# Configuração do Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API VitiBrasil",
        "description": "API para obtenção de dados sobre viticultura no Rio Grande do Sul",
        "version": "0.1.0"
    },
    "basePath": "/",
    "schemes": ["http", "https"],
    "consumes": ["application/json"],
    "produces": ["application/json"]
}

Swagger(app, config=swagger_config, template=swagger_template)

# Registra todas as rotas
register_production_routes(app)
register_processing_routes(app)
register_commercialization_routes(app)
register_import_routes(app)
register_export_routes(app)

@app.route('/')
def index():
    """
    Retorna informações da API.
    ---
    tags:
      - Informações
    responses:
      200:
        description: Informações da API obtidas com sucesso
        schema:
          type: object
          properties:
            name:
              type: string
              description: Nome da API
            version:
              type: string
              description: Versão da API
            endpoints:
              type: array
              items:
                type: object
                properties:
                  path:
                    type: string
                    description: Caminho do endpoint
                  methods:
                    type: array
                    items:
                      type: string
                    description: Métodos HTTP disponíveis
                  description:
                    type: string
                    description: Descrição do endpoint
                  parameters:
                    type: array
                    items:
                      type: object
                      properties:
                        name:
                          type: string
                          description: Nome do parâmetro
                        type:
                          type: string
                          description: Tipo do parâmetro
                        required:
                          type: boolean
                          description: Se o parâmetro é obrigatório
                        description:
                          type: string
                          description: Descrição do parâmetro
    """
    return jsonify({
        "name": "API VitiBrasil",
        "version": "0.1.0",
        "endpoints": [
            {
                "path": "/api/production",
                "methods": ["GET"],
                "description": "Obter dados de produção de vinho",
                "parameters": [
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            },
            {
                "path": "/api/processing",
                "methods": ["GET"],
                "description": "Obter dados de processamento de uvas para todas as categorias",
                "parameters": [
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            },
            {
                "path": "/api/processing/<category>",
                "methods": ["GET"],
                "description": "Obter dados de processamento de uvas para uma categoria específica",
                "parameters": [
                    {"name": "category", "type": "string", "required": True, "description": "Categoria de uva (viniferas, americanas, mesa, sem_classificacao)"},
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            },
            {
                "path": "/api/commercialization",
                "methods": ["GET"],
                "description": "Obter dados de comercialização para vinhos e derivados",
                "parameters": [
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            },
            {
                "path": "/api/import",
                "methods": ["GET"],
                "description": "Obter dados de importação para todas as categorias de produtos vitivinícolas",
                "parameters": [
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            },
            {
                "path": "/api/import/<category>",
                "methods": ["GET"],
                "description": "Obter dados de importação para uma categoria específica de produtos vitivinícolas",
                "parameters": [
                    {"name": "category", "type": "string", "required": True, "description": "Categoria de importação (vinhos_mesa, espumantes, uvas_frescas, uvas_passas, suco_uva)"},
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            },
            {
                "path": "/api/export",
                "methods": ["GET"],
                "description": "Obter dados de exportação para todas as categorias de produtos vitivinícolas",
                "parameters": [
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            },
            {
                "path": "/api/export/<category>",
                "methods": ["GET"],
                "description": "Obter dados de exportação para uma categoria específica de produtos vitivinícolas",
                "parameters": [
                    {"name": "category", "type": "string", "required": True, "description": "Categoria de exportação (vinhos_mesa, espumantes, uvas_frescas, suco_uva)"},
                    {"name": "year", "type": "integer", "required": False, "description": "Ano para obter os dados"}
                ]
            }
        ]
    })

if __name__ == '__main__':
    app.run(debug=True) 