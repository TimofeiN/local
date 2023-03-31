import sys

sale = sys.argv[1]
data = f'{sale}\n'

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(data)
