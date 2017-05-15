from flask import jsonify
from . import restroutes
from .stats import Stats

@restroutes.route('/stats/all', methods=['GET'])
def fullStats():
    stats = Stats()
    full_stats = stats.getStats()

    # file could not be found
    if len(full_stats) == 0:
        abort(404)

    return jsonify(full_stats)


@restroutes.route('/season', methods=['GET'])
def seasonName():
    stats = Stats()
    full_stats = stats.getStats()

    season_name = full_stats['Parity Season']
    # file could not be found
    if len(season_name) == 0:
        abort(404)

    return jsonify(season_name)

@restroutes.route('/stats/<int:player_id>', methods=['GET'])    # no spaces between int and player_id
def getPlayerStats(player_id):
    
    stats = Stats()
    full_stats = stats.getStats()

    if len(full_stats) == 0:    #id doesn't exist in database
        abort(404)
    
    # full_stats is a dictionary now, access it 
    for player in full_stats['Players']:
        if player['id'] == player_id:
            individual_stats = player
    
    return jsonify(individual_stats)