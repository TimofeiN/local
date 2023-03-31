def currency_rates(currency):
    from json import loads
    from requests import get
    from datetime import date

    dict_json = loads(get('https://www.cbr-xml-daily.ru/daily_json.js').text)
    currency = currency.upper()
    if currency in dict_json['Valute']:
        value = round(dict_json['Valute'][currency]['Value'], 2)
        date = date.fromisoformat(dict_json['Date'][:10])
        result = f'{date}, {value}'
    else:
        result = None
    print(result)
    return result


currency_rates('UsD')
currency_rates('ttt')
