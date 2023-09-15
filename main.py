from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    print(name)
    return render_template('index.html', name=name)


@app.route('/converter')
def converter():
    return '<h1>Converter</h1>'


@app.route('/articles')
def articles():
    return '<h1>Articles</h1>'


@app.route('/deposit')
def deposit():
    return '<h1>Deposit</h1>'


@app.route('/credit')
def credit():
    return '<h1>Credit</h1>'


@app.route('/info')
def info():
    return '<h1>Credit</h1>'