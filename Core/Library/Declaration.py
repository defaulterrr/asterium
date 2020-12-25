from .AddressTable import AddressTable

class Declaration:
    def __init__(self,name):
        self.name = name

    def eval(self, table: AddressTable, *argv):
        table.push(name=self.name)

    def __str__(self):
        self.str = "Declaration *"
        self.leftstr = "   \u21b3 Name: {0}".format(self.name)
        return self.str + "\n " + self.leftstr + "\n"

    def generate(self, table, ftable):
        pass