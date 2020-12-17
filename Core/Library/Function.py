from .FunctionTable import FunctionTable
from .AddressTable import AddressTable

class Function():
    def __init__(self, name, node):
        self.name = name
        self.node = node
    
    # evaluate addresses, check for previous definitions of a function and add a function to func namespace for calling
    def eval(self, atable: AddressTable, ftable: FunctionTable):
        ftable.addFunc(self.name, self.node)
        self.node.eval(atable,ftable)
        pass

    # generate function body to be later added to the end of the file for calling
    def generate(self, atable:AddressTable, ftable: FunctionTable):

        commands = self.node.generate(atable)
        print(commands)
        func = self.name + ":\n"
        if commands != None:
            func + commands
        return func
        