from converter import CurrencyConverter

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


@app.route('/get_converter_values', methods=['POST'])
def get_converter_values():
    data = request.form.to_dict()

    converter_instance = CurrencyConverter(data['dropdown_currency_from'])

    from_to_currency = converter_instance.convert(data['dropdown_currency_to'], float(data['amount_currency_from']))

    return render_template(
        'converted_currency.html',
        amount_from_currecny=data['amount_currency_from'],
        from_currency=data['dropdown_currency_from'],
        to_currency=data['dropdown_currency_to'],
        amount_to_currency=from_to_currency,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
