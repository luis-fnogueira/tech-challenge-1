"""
API Flask para dados do VitiBrasil.
"""

from flask import Flask
from flasgger import Swagger

from .production import register_production_routes
from .processing import register_processing_routes
from .commercialization import register_commercialization_routes
from .imports import register_import_routes
from .exports import register_export_routes

def create_app():
    """Cria e configura a aplicação Flask."""
    from .index import app
    return app 