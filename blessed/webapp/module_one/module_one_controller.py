from . import module_one_routes

@module_one_routes.route("/module_one_controller")
def module_one_controller():
    return "module one controller"