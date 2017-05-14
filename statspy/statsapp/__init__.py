from flask import Flask

app = Flask(__name__)   # creates application object 'app' of type flask (instantiating at higher level)
                        # rename app directory to another name (statsapp)a as to not confuse the package name with the variable (of type Flask)

# configurations
#app.config.from_object('config')


from statsapp import view # imports views module  (view.py)
                           # import at the end to avoid circular references