# get the user stats
import json
import os
import inspect

class Stats():
    
    stats_file = os.getcwd() + "\data\season_10_stats.json"

    # empty constructor method
    def __init__(self):
        self.x = 0

    def getStats(self):
        
        with open(self.stats_file) as json_file:
            json_stats = json.load(json_file)
        
        return json_stats