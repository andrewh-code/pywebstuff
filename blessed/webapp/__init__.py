from flask import Blueprint
webapp_routes = Blueprint('webapp_routes', __name__, url_prefix='/api/v1')

from .controller import *
from .module_one import *
from .authentication import *
