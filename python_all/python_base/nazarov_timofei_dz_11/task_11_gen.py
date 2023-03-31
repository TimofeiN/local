class GenId:
    def __init__(self):
        self.now = 1

    def __iter__(self):
        while True:
            yield self.now
            self.now += 1
