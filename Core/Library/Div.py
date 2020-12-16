from .BinaryOperation import BinaryOperation
from .AddressTable import AddressTable
class Div(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.address = ''

    def eval(self, addresstable):
        if self.address != "":
            return self.address
        else:
            self.address = addresstable.push(0)
            return self.address

    def generate(self, addresstable: AddressTable):
        self.cmds = []
        self.left.eval(addresstable)
        self.right.eval(addresstable)
        self.cmds.append(self.left.generate(addresstable))
        self.cmds.append(self.right.generate(addresstable))
        self.cmds.append("ld A," + str(self.left.eval(addresstable)) + ";\n")
        self.cmds.append("div A," + str(self.right.eval(addresstable)) + ";\n")
        self.cmds.append("st A," + str(self.address) + ";\n")
        #print(self.cmds)
        cmds = "".join(self.cmds)
        return cmds