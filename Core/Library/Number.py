from rply.token import BaseBox

class Number(BaseBox):
    def __init__(self,value):
        self.value = value
        self.address = ""

    def reserve(self):
        """
        Reserve a word
        """
        # <name>: word <word>
        # get unique name
        # self.address = get_random_string()
        # set its value
        # push to name table
        # set self.address = unique name

    def __str__(self):
        return "Number: {0}".format(self.value)

    def eval(self, addresstable, ftable, namespace=""):
        #return self.value
        # self.address = addresstable.push(self.value)
        # print(self.address + " " + "word" + " " + str(self.value) + "\n")
        # if self.address != "":
        #     return self.address
        # else:
        #     self.address = addresstable.push(self.value)
        #     return self.address
        assert self.address == ""
        namespace = "const_" + namespace
        addresstable.push(value=self.value,namespace=namespace)
        pass

    def generate(self, addresstable, ftable):
        return "\n"
