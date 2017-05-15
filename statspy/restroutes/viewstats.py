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

@restroutes.route('/stats/all', methods=['GET'])
def fullStats():
    stats = Stats()
    full_stats = stats.getStats()

    # file could not be found
    if len(full_stats) > 0:
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

@restroutes.route('/stats/<int:player_id>', methods=['GET'])    # no spaces between int and player_id
def getPlayerStats(player_id):
    
    stats = Stats()
    full_stats = stats.getStats()

    if len(full_stats) == 0:    #id doesn't exist in database
        payload = not_found()
    else:
        # full_stats is a dictionary now, access it 
        for player in full_stats['Players']:
            if player['id'] == player_id:
                individual_stats = player
        payload = jsonify(individual_stats)
    
    return payload

@restroutes.route('/stats/leaders', methods=['GET'])
def getLeaders():
    
    stats = Stats()
    full_stats = stats.getStats()
    
    goal_leaders = []
    assist_leaders = []
    second_assist_leaders = []
    defensive_leaders = []
    throwaway_leaders = []
    receiver_leaders = []

    leaders_dict = {}
    lowest_goals = 0

    for player in full_stats['Players']:
        goal_leaders.append([player['Name'], int(player['Stats']['Goals'])])
        assist_leaders.append([player['Name'], int(player['Stats']['Assists'])])
        second_assist_leaders.append([player['Name'], int(player['Stats']['2nd Assists'])])
        defensive_leaders.append([player['Name'], int(player['Stats']['Ds'])])
        throwaway_leaders.append([player['Name'], int(player['Stats']['Throwaways'])])
        receiver_leaders.append([player['Name'], int(player['Stats']['Receiver Error'])])
        

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

    
    leaders_dict['Goals'] = goal_leaders
    leaders_dict['Assists'] = assist_leaders
    leaders_dict['2nd Assists'] = second_assist_leaders
    leaders_dict['Ds'] = second_assist_leaders
    leaders_dict['Throwaways'] = throwaway_leaders
    leaders_dict['Recever Error'] = receiver_leaders

    return jsonify(leaders_dict)

