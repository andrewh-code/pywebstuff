from flask import Blueprint
authentication_routes = Blueprint('authentication_routes', __name__, url_prefix='/api/v1/authentication')

from .authentication_controller import *