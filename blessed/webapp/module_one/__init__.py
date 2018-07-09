from flask import Blueprint
module_one_routes = Blueprint('module_one_routes', __name__, url_prefix='/api/v1/module_one')

from .module_one_controller import *