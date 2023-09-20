from converter import CurrencyConverter

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/converter')
def converter():
    return render_template('converter.html', A='kek')


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


@app.route('/converted_values', methods=['POST'])
def converted_values():
    data = request.form.to_dict()
    amount_from_currency = float(data['inputAmountCurrencyFrom'])
    from_currency = data['SelectCurrencyFrom']
    to_currency = data['SelectCurrencyTo']
    print(data)

    converter_instance = CurrencyConverter(from_currency)
    result = converter_instance.convert(to_currency, amount_from_currency)

    response_data = {
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount_from_currency': amount_from_currency,
        'converted_amount': result,

    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
