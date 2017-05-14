from flask import Flask
from flask import request

app = Flask(__name__)

# define routes
@app.route('/')
def index():
    return "hello, world"

@app.route('/hello')
def hello():
    if 'name' in request.args:
        return request.args['name']
    else:
        return 'hello'

# main
if __name__ == '__main__':
    app.run(debug=True)