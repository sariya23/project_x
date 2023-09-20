document.getElementById('form').addEventListener('submit', function(event) {
        event.preventDefault()
        const inputAmountCurrencyFrom = document.getElementById('amount_currency_from').value;
        const SelectCurrencyFrom = document.getElementById('dropdown_currency_from').value;
        const SelectCurrencyTo = document.getElementById('dropdown_currency_to').value;

        const formData = new FormData();
        formData.append('inputAmountCurrencyFrom', inputAmountCurrencyFrom);
        formData.append('SelectCurrencyFrom', SelectCurrencyFrom);
        formData.append('SelectCurrencyTo', SelectCurrencyTo);

        fetch('/converted_values', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result_text').textContent = `Из ${data.amount_from_currency}${data.from_currency} получается ${data.converted_amount}${data.to_currency}`;
            document.getElementById('rate').textContent = `1${data.from_currency} is ${data.rate} ${data.to_currency}`
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
});