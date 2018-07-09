# import libraries and dependencies
from flask import Flask
from webapp import webapp_routes
from webapp.module_one import module_one_routes

app = Flask(__name__)
############################################################
#
# here, run the main server
#
############################################################

@app.route("/")
def index():
    return "you are at the index"

if __name__ == '__main__':
    app.register_blueprint(webapp_routes)
    app.register_blueprint(module_one_routes)
    app.run(host='localhost', port=5000, debug=True)
