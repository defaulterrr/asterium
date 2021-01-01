from .BinaryOperation import BinaryOperation
from .AddressTable import AddressTable
from .FunctionTable import FunctionTable

class Mul(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.address = ''

    def eval(self, addresstable: AddressTable, ftable: FunctionTable, namespace=""):
        assert self.address == ""
        self.address = addresstable.push(namespace)

    def __str__(self):
        self.str = "Multiply, address: {0}".format(self.address)
        self.leftstr = " \u21b3" + self.left.__str__()
        self.rightstr = " \u21b3" + self.right.__str__()
        return self.str + "\n " + self.leftstr + "\n " + self.rightstr + "\n"

    def generate(self, addresstable, ftable):
        self.cmds = []
        self.left.eval(addresstable, ftable)
        self.right.eval(addresstable, ftable)
        self.cmds.append(self.left.generate(addresstable, ftable))
        self.cmds.append(self.right.generate(addresstable, ftable))
        self.cmds.append("ld A," + str(self.left.eval(addresstable, ftable)) + ";\n")
        self.cmds.append("mul A," + str(self.right.eval(addresstable, ftable)) + ";\n")
        self.cmds.append("st A," + str(self.address) + ";\n")
        cmds = "".join(self.cmds)
        return cmds