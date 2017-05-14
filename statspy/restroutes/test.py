import os
import inspect

curdir = os.getcwd()
print(curdir)

print (inspect.stack()[0][1])   

file = curdir + "data/season_10_stats.json"
print(file)