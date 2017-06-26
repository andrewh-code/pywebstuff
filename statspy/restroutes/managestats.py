from flask import jsonify
from flask import Response
from flask import request
from . import restroutes
from .stats import Stats

@restroutes.errorhandler(404)
def not_found(error=None):
    server_message = {
        "status": 404,
        "message": "sorry the requested url cannot be found: " + request.url
    }

    resp = jsonify(server_message)
    resp.status_code = 404

    return resp

@restroutes.errorhandler(400)
def bad_request(error = None):
    server_message = {
        "status": 400,
        "message": "Sorry, the server cannot process the reuquest: " + request.url
    }

    resp = jsonify(server_message)
    resp.status_code = 400

    return resp

@restroutes.errorhandler(415)
def unsupported_media_type(error = None):
    server_message = {
        "status": 415,
        "message": "Serve does not accept the content-type"
    }
    resp = jsonify(server_message)
    resp.status_code = 415
    return resp

@restroutes.errorhandler(405)
def method_not_allowed(error = None):
    server_message = {
        "status": 405,
        "message": "Http method not allowed"
    }
    resp = jsonify(server_message)
    resp.status_code = 405
    return resp

@restroutes.route('/adding', methods=['POST'])
def add_test():
    message = {"message": "success"}
    resp = jsonify(message)
    resp.status_code = 200
    return resp 


@restroutes.route('/manage/<int:player_id>', methods=['POST'])
def addPlayer(player_id):
    stats = Stats()
    full_stats = stats.getStats()
    print(__file__, "debug")
    player_found = False


    # file could not be found
    if (len(full_stats) == 0):
        server_message = {
            "status": 400,
            "message": "Sorry, unable to get the stats" 
        }

        resp = jsonify(server_message)
        resp.status_code = 400
        return resp
    
    # check the content type (only accepts json)
    if (request.headers['Content-Type'] != 'application/json'):
        resp = unsupported_media_type()
        return resp
    
    request_data = request.get_json()
    # check for empty payload
    if len(request_data) == 0:  
        server_message = {
            "status": 400,
            "message": "Sorry, no data in the payload request" 
        }

        resp = jsonify(server_message)
        resp.status_code = 400
        return resp

    # check to see if player already exists in the "database"
    for player in full_stats['Players']:
        if player['id'] == player_id:
            player_found = True
            message = {"status": 200,
                        "Message": "player ID already exists, choose another one"} 
            resp = jsonify(message)
            resp.status_code = 200
            break

    # if player doesn't exist, create them
    if player_found == False:
        old_count = len(full_stats['Players'])
        full_stats['Players'].append(request_data)   # need to do some valid error check
    
        # do some more validation here (check to see if json format is good and they put in everything correctly
        if (len(full_stats['Players']) == old_count + 1):
            resp = jsonify(full_stats)
            resp.status_code = 201
        else:
            resp = bad_request()
        
    return resp 

        
@restroutes.route('/manage/<int:player_id>', methods=["DELETE"])
def delete_player(player_id):
    stats = Stats()
    full_stats = stats.getStats()
    print(__file__, "debug")
    player_found = False
    count = 0

    # check to see if player already exists in the "database"
    for player in full_stats['Players']:
        if player['id'] == player_id:
            player_found = True
            break 
        count = count + 1

    if (player_found == False):
        message = { "status": 404,
                    "message": "player id not found"}
        resp = jsonify(message)
        resp.status_code = 404
    else:
        # this is where you delete the player from the database 
        full_stats['Players'].pop(count)
        resp = jsonify(full_stats)
        resp.status_code = 200
    
    return resp



    

    




