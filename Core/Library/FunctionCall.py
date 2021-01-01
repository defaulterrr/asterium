from .AddressTable import AddressTable
from .FunctionTable import FunctionTable

class FunctionCall():
    def __init__(self,name):
        self.calledName = name

    def __str__(self):
        return "Call to function {0}".format(self.calledName)

    def eval(self, addresstable: AddressTable, ftable: FunctionTable, namespace=""):
        pass