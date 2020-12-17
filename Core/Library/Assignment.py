from .AddressTable import AddressTable
from rply.token import BaseBox
from .BinaryOperation import BinaryOperation

class Assignment(BinaryOperation):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.assignmentAddress = ''
        self.sourceAddress = ''

    def eval(self, addresstable: AddressTable, ftable):
        # if self.address !="":
        #     return self.address
        # else:
        #     self.address = addresstable.push(name=self.left.eval())
        # return self.address
        self.assignmentAddress = self.left.eval().getstr()
        
        # print("______")
        # print("Assignment address: " + self.assignmentAddress)
        # print("Source address: " + self.sourceAddress)
        # print("______")
        if addresstable.isPresent(self.assignmentAddress):
            self.sourceAddress = self.right.eval(addresstable, ftable)
        else:
            raise ValueError("Such variable is not present up to this point")

    def generate(self, addresstable: AddressTable, ftable):
        self.cmds = []
        # self.cmds.append(self.left.generate(addresstable))
        self.cmds.append(self.right.generate(addresstable, ftable))
        self.cmds.append("ld A," + str(self.right.eval(addresstable, ftable)) + ";\n")
        self.cmds.append("st A," + str(self.left.eval().getstr()))
        print(self.cmds)
        cmds = "".join(self.cmds)
        return cmds
