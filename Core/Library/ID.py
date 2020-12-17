class ID:
    def __init__(self, name):
        self.name = name

    def eval(self):
        return self.name

    def generate(self, addresstable, ftable):
        return self.name
