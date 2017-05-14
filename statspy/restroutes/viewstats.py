from flask import jsonify
from . import restroutes
from .stats import Stats

@restroutes.route('/fullstats', methods=['GET'])
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

#@restroutes.route('/stats/')