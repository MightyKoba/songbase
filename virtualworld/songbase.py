from flask import flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'

@app.route('/user/<strring:name>')
def home():
    return '<h1>hello %s</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
    
