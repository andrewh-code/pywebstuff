import os
import sys
import inspect
from statsapp import app
from restroutes import *

# import the 'app' variable from the statsapp package (defined in __init__.py)

# in order to modularize the rest api, should put in a routes folder (use blueprints)
# 
print (__file__)
print (os.path.realpath(__file__))
print (os.path.abspath(__file__))
print (os.path.basename(__file__))
app.register_blueprint(restroutes) 
app.run(debug=True)