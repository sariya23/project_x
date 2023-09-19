import requests
import os


class CurrencyConverter:
    """
    Класс представляет возможно конвертации валют
    через API https://www.exchangerate-api.com/docs/free.
    """

    def __init__(self, url):
        if requests.get(url).status_code == 404:
            raise ValueError('Smth wrong 404')
        self.data = requests.get(url).json()
        self.currencies = self.data['conversion_rates']

    def converter(self, from_currency: str, to_currency: str, initial_amount: int | float):
        amount = 0

        if from_currency != 'USD':
            amount = initial_amount / self.currencies[from_currency]

        amount = round(initial_amount * self.currencies[to_currency], 4)
        return amount


a = CurrencyConverter(f'https://v6.exchangerate-api.com/v6/{os.environ["API_KEY"]}/latest/EUR')
print(a.converter('EUR', 'RUB', 1))