class FunctionTable():
    def __init__(self):
        self.addresses = []
        self.functions = {}

    def addFunc(self,name, func):
        if not name in self.addresses:
            self.addresses.append(name)
        else:
            raise ValueError("Function with such name was already declared: " + name)
        self.function[name] = func

    def generate(self):
        funcs = []
        for name in self.addresses:
            cmds = self.functions[name].generate()
            funcs.append(cmds)

        return "".join(funcs)
