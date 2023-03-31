on_stock = {}


class Stock:

    @staticmethod
    def show_stock():
        return f'на складе {on_stock}'


class Technique:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f'Tech {Technique.__name__}'

    def move_to_stock(self, count):
        on_stock.update({f'{self.__str__}': {self.brand: count}})


class Printer(Technique):
    def __init__(self, brand):
        super().__init__(brand)

    def __str__(self):
        super(Printer, self).__str__()


hp = Printer('hp')

Technique.move_to_stock(hp, 60)

print(Stock.show_stock())