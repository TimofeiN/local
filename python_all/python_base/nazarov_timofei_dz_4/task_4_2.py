import json
from requests import get


def currency_rates(currency):
    dict_json = json.loads(get('https://www.cbr-xml-daily.ru/daily_json.js').text)
    currency = currency.upper()
    if currency in dict_json['Valute']:
        result = round(dict_json['Valute'][currency]['Value'], 2)
    else:
        result = None
    return result


print(currency_rates('usd'))
print(currency_rates('Eur'))
