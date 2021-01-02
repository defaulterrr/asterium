from .AddressTable import AddressTable
from .FunctionTable import FunctionTable

class Declaration:
    def __init__(self,name):
        self.name = name
        self.address = ""

    def eval(self, table: AddressTable, functiontable: FunctionTable, namespace=""):
        if namespace == "":
            namespace = "global"
        if table.isPresent(self.name, namespace):
            raise ValueError("Variable is already declared")
        else:
            self.address = table.push_named(namespace=namespace, name=self.name)

    def __str__(self):
        self.str = "Declaration *"
        self.leftstr = "   \u21b3 Name: {0}".format(self.name)
        return self.str + "\n " + self.leftstr + "\n"

    def generate(self, table, ftable):
        pass