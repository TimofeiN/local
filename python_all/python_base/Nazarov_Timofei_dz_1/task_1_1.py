duration = int(input('Продолжительность сек. = '))
s = duration % 60

if 0 <= duration < 60:
    print(f'{duration} сек')
elif 60 <=  duration < 3600:
    m = duration // 60
    print(f'{m} мин {s} сек')
elif duration >= 3600 and duration < 86400:
    h = duration // 3600
    m = duration % 3600 // 60
    print(f'{h} час {m} мин {s} сек')
else:
    d = duration // 86400
    h = duration % 86400 // 3600
    m = duration % 3600 // 60
    print(f'{d} дн {h} час {m} мин {s} сек')
