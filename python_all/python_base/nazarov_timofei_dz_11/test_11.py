class NumberErr(Exception):
    def __init__(self, txt):
        self.txt = txt
    def __str__(self, data):
        return f'{data} not a num'

numbers = []
data = None
while True:
    data = input('Введи число stop для завершения: ')
    if data == 'stop':
        print(numbers)
        break
    try:
        data = int(data)
    except NumberErr as int_er:
        print(int_er)
    else:
        numbers.append(int(data))
