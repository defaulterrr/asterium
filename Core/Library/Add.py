from .BinaryOperation import BinaryOperation

class Add(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, right)
        self.address = ''


    def eval(self, addresstable, ftable):
        # address 1
        # address 2
        # ld A, address1;
        # add A, address2;  // -> a
        # st A, address3;
        # self.resultAddress = get_random_string()
        if self.address != "":
            return self.address
        else:
            self.address = addresstable.push(0)
            return self.address

    def generate(self, addresstable, ftable,  *argv):
        self.cmds = []
        self.left.eval(addresstable, ftable)
        self.right.eval(addresstable, ftable)
        self.cmds.append(self.left.generate(addresstable, ftable))
        self.cmds.append(self.right.generate(addresstable, ftable))
        self.cmds.append("ld A," + str(self.left.eval(addresstable, ftable)) + ";\n")
        self.cmds.append("add A," + str(self.right.eval(addresstable, ftable)) + ";\n")
        self.cmds.append("st A," + str(self.address) + ";\n")
        cmds = "".join(self.cmds)
        return cmds