class FunctionTable():
    def __init__(self):
        self.addresses = []
        self.functions = {}

    def addFunc(self,name, func, namespace=""):
        if not name in self.addresses:
            self.addresses.append(name)
        else:
            raise ValueError("Function with such name was already declared: " + name)
        self.functions[name] = func

    def generate(self,atable,ftable):
        funcs = []
        for name in self.addresses:
            cmds = self.functions[name].generate(atable,ftable)
            funcs.append(cmds)

        return "".join(funcs)

    def __str__(self):
        output = "Function table_______\n"
        for address in self.addresses:
            output = output + "Address: {}\n".format(address)
        return output
