from flask import Blueprint

maestros = Blueprint(
    'maestros',
    __name__,
    template_folder = 'template',
    static_folder = 'static')
from . import routes