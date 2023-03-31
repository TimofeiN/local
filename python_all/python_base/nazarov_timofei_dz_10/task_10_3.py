from abc import abstractmethod


class Cell:
    def __init__(self, cells, line=0):
        self.cells = cells
        self.line = line

    def __str__(self):
        return f'cell with {self.cells} units'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            print(f'Unpossible to subtract difference less than 0')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def __truediv__(self, other):
        return Cell(self.cells / other.cells)

    @abstractmethod
    def make_order(self, cells, line):
        x = cells // line
        y = cells % line
        output = (f'*' * line + f"\\n") * x + f'*' * y
        return output


first_cell = Cell(40)
second_cell = Cell(30)

res = first_cell + second_cell
print(res)
print(first_cell.make_order(12, 5))
