class Date:
    def __init__(self, date_str):
        self.date = date_str

    @classmethod
    def date_to_num(cls, date):
        date_lst = (date.split('-'))
        day = int(date_lst[0])
        month = int(date_lst[1])
        year = int(date_lst[2])
        return day, month, year

    @staticmethod
    def valid_date(date):
        date_num = Date.date_to_num(date)
        day = date_num[0]
        month = date_num[1]
        year = date_num[2]
        if day <= 0 or day > 31:
            res = f'{date} is not valid date, enter day from 1 to 31'
        elif month <= 0 or month > 12:
            res = f'{date} is not valid date, enter month from 1 to 12'
        elif month == 2 and day > 29:
            res = f'{date} is not valid date, second month has max 29 days'
        elif year < 0:
            res = f'{date} is not valid date, enter year > 0'
        else:
            res = f'{date} is valid date'
        return res


test_date = '32-14-1986'
dt = Date

print(dt, type(dt))
print(dt.date_to_num(test_date))
print(dt.valid_date(test_date))
