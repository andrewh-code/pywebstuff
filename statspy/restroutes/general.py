from flask import jsonify
from . import restroutes
from .stats import Stats

@restroutes.route('/hello')
def hello():
    return 'hello fromn stats'

