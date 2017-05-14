from statsapp import app

@app.route('/')
def hello():
    return 'hello from view'

@app.route('/index')
def index():
    return 'welcome to the index page'
 