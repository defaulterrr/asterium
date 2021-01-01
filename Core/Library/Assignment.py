from .AddressTable import AddressTable
from .FunctionTable import FunctionTable
from rply.token import BaseBox
from .BinaryOperation import BinaryOperation
import textwrap

class Assignment(BinaryOperation):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.assignmentAddress = ''
        self.sourceAddress = ''

    def eval(self, addresstable: AddressTable, functiontable: FunctionTable, namespace=""):
        self.left.eval(addresstable, functiontable, namespace)
        self.right.eval(addresstable, functiontable, namespace)

    def __str__(self):
        self.assignmentAddressStr = textwrap.indent("Assignment address: {0}".format(self.left.__str__()),"    ")
        self.sourceAddressStr = textwrap.indent("Source address: {0}".format(self.right.__str__()),"    ")
        return "Assignment " + "\n" + self.assignmentAddressStr + "\n" + self.sourceAddressStr

    def generate(self, addresstable: AddressTable, ftable):
        # self.cmds = []
        # # self.cmds.append(self.left.generate(addresstable))
        # self.cmds.append(self.right.generate(addresstable, ftable))
        # self.cmds.append("ld A," + str(self.right.eval(addresstable, ftable)) + ";\n")
        # self.cmds.append("st A," + str(self.left.eval().getstr()))
        # print(self.cmds)
        # cmds = "".join(self.cmds)
        # return cmds
        pass
