class ZeroDiv(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите делимое: ')
b = input('Введите делитель: ')

try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise ZeroDiv('Деление на ноль!')
except ValueError:
    print('Введено не число')
except ZeroDiv as err:
    print(err)
else:
    c = a / b
    print(f'{a} / {b} = {c}')