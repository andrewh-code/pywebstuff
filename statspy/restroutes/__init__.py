from flask import Blueprint
restroutes = Blueprint('routes', __name__, url_prefix='/api/v1')

from .general import *
from .viewstats import *
from .managestats import *