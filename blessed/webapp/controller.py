from . import webapp_routes

@webapp_routes.route("/controller")
def controller():
    return "controller response" 