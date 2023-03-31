import re
RE_DATA_VAL = re.compile(r'^\d+([,.]\d+)*$')


class NumberErr(Exception):
    def __init__(self, txt):
        self.txt = txt


numbers = []
data = None
while True:
    data = input('Введи число или stop для завершения: ')
    if data == 'stop':
        print(numbers)
        break
    else:
        try:
            if not RE_DATA_VAL.match(data):
                raise NumberErr(f'{data} not a number')
        except NumberErr as e:
            print(e)
        else:
            data = float(data)
            try:
                data / round(data)
            except ZeroDivisionError:
                numbers.append(int(data))
            else:
                if data / round(data) != 1:
                    numbers.append(data)
                else:
                    numbers.append(int(data))
