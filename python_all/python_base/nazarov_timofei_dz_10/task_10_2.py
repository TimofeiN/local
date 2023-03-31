from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def textile_calc(self):
        pass


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    @property
    def textile_calc(self):
        textile = (2 * self.param) + 0.3
        return textile


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    @property
    def textile_calc(self):
        textile = (self.param / 6.5) + 0.5
        return textile


suit = Suit(180)
print(suit.textile_calc)
coat = Coat(66)
print(coat.textile_calc)
