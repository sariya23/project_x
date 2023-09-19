from urllib.parse import urljoin

import requests
import os


class CurrencyConverter:
    """
    Класс представляет возможно конвертации валют
    через API https://www.exchangerate-api.com/docs/free.
    """

    BASE_URL = f'https://v6.exchangerate-api.com/v6/{os.environ["API_KEY"]}/latest/'

    def __init__(self, from_currency):
        self.url = urljoin(self.BASE_URL, from_currency)

        if requests.get(self.url).status_code == 404:
            raise ValueError('Smth wrong 404')
        self.data = requests.get(self.url).json()
        self.currencies = self.data['conversion_rates']

    def convert(self, to_currency: str, initial_amount: int | float):
        """
        Переводит из валюты, переданной в инициализаторе
        в to_currency
        """
        amount = round(initial_amount * self.currencies[to_currency], 4)
        return amount


if __name__ == '__main__':
    # Насколько я понял, в конце URL нужно указывать из какой валюты переводим
    a = CurrencyConverter('USD')
    print(a.convert('RUB', 1))
