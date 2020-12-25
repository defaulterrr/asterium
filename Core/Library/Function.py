from .FunctionTable import FunctionTable
from .AddressTable import AddressTable
import textwrap

class Function():
    def __init__(self, name, node):
        self.name = name
        self.node = node
    
    # evaluate addresses, check for previous definitions of a function and add a function to func namespace for calling
    def eval(self, atable: AddressTable, ftable: FunctionTable):
        ftable.addFunc(self.name, self.node)
        self.node.eval(atable,ftable)
        pass

    def __str__(self):
        strstr = self.node.__str__()
        self.nodestr = textwrap.indent(" Function Node: {0}".format(strstr),"    ")
        # self.nodestr = textwrap.indent(" Function Node: {0}".format(strstr),4)
        return "Function declaration with name \"{0}\"".format(self.name) + "\n" + self.nodestr
    # generate function body to be later added to the end of the file for calling
    def generate(self, atable:AddressTable, ftable: FunctionTable):

        commands = self.node.generate(atable,ftable)
        print(commands)
        func = self.name + ":\n"
        if commands != None:
            func + commands
        return func
        