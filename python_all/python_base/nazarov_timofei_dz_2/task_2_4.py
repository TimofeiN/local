position_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for v in position_name:
    v = v.split(' ')
    name = v[-1].capitalize()
    print(f'Привет, {name}!')
