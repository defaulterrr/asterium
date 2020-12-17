from .AddressTable import AddressTable

class Declaration:
    def __init__(self,name):
        self.name = name

    def eval(self, table: AddressTable):
        table.push(name=self.name)

    def generate(self, table):
        pass