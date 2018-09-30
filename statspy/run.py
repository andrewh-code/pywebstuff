import os
import sys
import inspect
from restroutes import *
from flask import Flask

# import the 'app' variable from the statsapp package (defined in __init__.py)

# in order to modularize the rest api, should put in a routes folder (use blueprints)
# 
app = Flask(__name__)



# define routes
@app.route('/')
def index():
    return "hello, world"


app.register_blueprint(restroutes) 
app.run(debug=True)