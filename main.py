from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/converter')
def converter():
    return render_template('converter.html')


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


@app.route('/read-form', methods=['POST'])
def read_form():
    data = request.form.to_dict()
    print(data)
    return data