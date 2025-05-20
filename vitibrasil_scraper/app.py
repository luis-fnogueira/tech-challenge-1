"""
Entry point for Vercel deployment.
"""

from flask import Flask
from flasgger import Swagger

from api.production import register_production_routes
from api.processing import register_processing_routes
from api.commercialization import register_commercialization_routes
from api.imports import register_import_routes
from api.exports import register_export_routes
from api.index import register_index_route

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
register_index_route(app)


if __name__ == "__main__":
    app.run() 