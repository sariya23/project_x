from converter import CurrencyConverter

from flask import Flask, render_template, request, jsonify

from utils import get_db_connection

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
    conn = get_db_connection('database.db')
    if conn:
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
    else:
        posts = []
    print(posts)
    return render_template('articles.html', posts=posts)


@app.route('/deposit')
def deposit():
    return render_template('deposit.html')


@app.route('/credit')
def credit():
    return render_template('credit.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/converted_values', methods=['POST'])
def converted_values():
    data = request.form.to_dict()
    amount_from_currency = float(data['inputAmountCurrencyFrom'])
    from_currency = data['SelectCurrencyFrom']
    to_currency = data['SelectCurrencyTo']
    print(data)

    converter_instance = CurrencyConverter(from_currency)
    result, rate = converter_instance.convert(to_currency, amount_from_currency)

    response_data = {
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount_from_currency': amount_from_currency,
        'converted_amount': result,
        'rate': rate,
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
