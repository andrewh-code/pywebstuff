from . import authentication_routes

@authentication_routes.route("/authentication")
def module_one_controller():
    return "authentication conmtroller"