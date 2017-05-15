import os
import sys
import inspect
from statsapp import app
from restroutes import *

# import the 'app' variable from the statsapp package (defined in __init__.py)

# in order to modularize the rest api, should put in a routes folder (use blueprints)
# 
app.register_blueprint(restroutes) 
app.run(debug=True)