from .AddressTable import AddressTable
from .FunctionTable import FunctionTable

class ID:
    def __init__(self, name):
        self.name = name

    def eval(self, addresstable: AddressTable, ftable: FunctionTable, namespace=""):
        pass
        # nothing here yet

    def generate(self, addresstable, ftable):
        pass
