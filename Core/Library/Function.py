from .FunctionTable import FunctionTable
from .AddressTable import AddressTable

class Function():
    def __init__(self, name, node):
        self.name = name
        self.node = node
    
    # evaluate addresses, check for previous definitions of a function and add a function to func namespace for calling
    def eval(self, table: FunctionTable, atable: AddressTable):
        table.addFunc(self.name)
        self.node.eval(atable)
        pass

    # generate function body to be later added to the end of the file for calling
    def generate(self, atable:AddressTable):

        commands = self.node.generate(atable)
        func = self.name + ":\n"
        return func + commands
        