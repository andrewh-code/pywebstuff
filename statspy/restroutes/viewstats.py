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

@restroutes.route('/stats/all', methods=['GET'])
def fullStats():
    stats = Stats()
    full_stats = stats.getStats()

    # file could not be found
    if len(full_stats) == 0:
        payload = not_found()
    else:
        payload = jsonify(full_stats)

    return payload


@restroutes.route('/season', methods=['GET'])
def seasonName():
    stats = Stats()
    full_stats = stats.getStats()

    season_name = full_stats['Parity Season']
    # file could not be found
    if len(season_name) == 0:
        payload = not_found()
    else:
        payload = jsonify(season_name)

    return payload

@restroutes.route('/stats/leaders', methods=['GET'])
def getLeaders():
    
    stats = Stats()
    full_stats = stats.getStats()
    
    if len(full_stats) == 0:
        return not_found()
    
    goal_leaders = []
    assist_leaders = []
    second_assist_leaders = []
    defensive_leaders = []
    throwaway_leaders = []
    receiver_leaders = []
    salary_leaders = []
    win_leaders = []

    leaders_dict = {}
    lowest_goals = 0

    for player in full_stats['Players']:
        goal_leaders.append([player['Name'], int(player['Stats']['Goals'])])
        assist_leaders.append([player['Name'], int(player['Stats']['Assists'])])
        second_assist_leaders.append([player['Name'], int(player['Stats']['2nd Assists'])])
        defensive_leaders.append([player['Name'], int(player['Stats']['Ds'])])
        throwaway_leaders.append([player['Name'], int(player['Stats']['Throwaways'])])
        receiver_leaders.append([player['Name'], int(player['Stats']['Receiver Error'])])
        salary_leaders.append([player['Name'], player['Stats']['Salary']])
        win_leaders.append([player['Name'], float(player['Stats']['Wins'])])
        

    goal_leaders = sorted(goal_leaders, key=lambda x: x[1], reverse=True)
    goal_leaders = goal_leaders[:5]

    assist_leaders = sorted(assist_leaders, key=lambda x: x[1], reverse=True)
    assist_leaders = assist_leaders[:5]

    second_assist_leaders = sorted(second_assist_leaders, key=lambda x: x[1], reverse=True)
    second_assist_leaders = second_assist_leaders[:5]

    defensive_leaders = sorted(defensive_leaders, key=lambda x: x[1], reverse=True)
    defensive_leaders = defensive_leaders[:5]

    throwaway_leaders = sorted(throwaway_leaders, key=lambda x: x[1], reverse=True)
    throwaway_leaders = throwaway_leaders[:5]

    receiver_leaders = sorted(receiver_leaders, key=lambda x: x[1], reverse=True)
    receiver_leaders = receiver_leaders[:5]

    salary_leaders = sorted(salary_leaders, key=lambda x: x[1], reverse=True)
    salary_leaders = salary_leaders[:5]

    win_leaders = sorted(win_leaders, key=lambda x: x[1], reverse=True)
    win_leaders = win_leaders[:5]

    
    leaders_dict['Goals'] = goal_leaders
    leaders_dict['Assists'] = assist_leaders
    leaders_dict['2nd Assists'] = second_assist_leaders
    leaders_dict['Ds'] = second_assist_leaders
    leaders_dict['Throwaways'] = throwaway_leaders
    leaders_dict['Recever Error'] = receiver_leaders
    leaders_dict['Salary'] = salary_leaders
    leaders_dict['Wins'] = win_leaders

    return jsonify(leaders_dict)


@restroutes.route('/stats/<int:player_id>', methods=['GET', 'PUT'])    # no spaces between int and player_id
def getPlayerStats(player_id):
    
    # variables
    stats = Stats()
    full_stats = stats.getStats()
    player_found = False

    if len(full_stats) == 0:    #id doesn't exist in database
        payload = not_found()
        return payload 
    
    if not request.get_json():
        payload = not_found()
        return payload 

    if (request.method == 'GET'):        
        # full_stats is a dictionary now, access it 
        for player in full_stats['Players']:
            if player['id'] == player_id:
                individual_stats = player
        payload = jsonify(individual_stats)
        return payload 
    
    # updating a user
    if (request.method == 'PUT'):
        request_data = request.get_json()
       
        for player in full_stats['Players']:
            if player['id'] == player_id:
                player_found = True
                break

        if player_found == True:
            # iterate over body to get the key
            for key in request_data:
                if key in player['Stats']:
                    player['Stats'][key] = request_data[key]
            
            payload = jsonify(player)
            return payload
            # go through the process of updating the database here
        else:
            return not_found()

    return bad_request()