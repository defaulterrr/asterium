class FunctionCall():
    def __init__(self,name):
        self.calledName = name

    def __str__(self):
        return "Call to function {0}".format(self.calledName)