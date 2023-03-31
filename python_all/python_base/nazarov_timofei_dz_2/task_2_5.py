prices = [77.04, 35.24, 2.3, 67, 87.1, 15.75, 46.4, 7.77, 80.88, 43.84, 26.93, 86.93, 44.44, 57.45, 65.23]
print(prices, ' id -', id(prices))

for i in range(len(prices)):
    price = float(prices[i])
    price = f'{int(price // 1):02d} руб {int(round(((price%1)*100), 2)):02d} коп'
    prices[i] = price
message = ', '.join(prices)
print(message)

prices.sort()
print(prices, ' id -', id(prices))

prices_rev = list(reversed(prices))
print(prices_rev, ' id -', id(prices_rev))

# Top 5
print(prices_rev[:5])
