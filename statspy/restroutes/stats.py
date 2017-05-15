# get the user stats
import json
import os
import inspect

# simulate the database stuff
class Stats():
    
    stats_file_name = "test_data.json"
    stats_file = os.getcwd() + "\\data\\" + stats_file_name # remember the escape character

    # empty constructor method
    def __init__(self):
        self.x = 0

    def getStats(self):
        print("stats file is: ", self.stats_file)
        with open(self.stats_file) as json_file:
            json_stats = json.load(json_file)
        
        return json_stats