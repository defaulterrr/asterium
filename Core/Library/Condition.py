class Condition:
    def __init__(self, operation, leftOp, rightOp):
        self.operation =  operation
        self.leftOp = leftOp
        self.rightOp = rightOp

    def __str__(self):
        import textwrap
        self.str = "Condition *"
        operation = textwrap.indent("   \u21b3" + self.operation.__str__(),"  ")
        leftOp = textwrap.indent("   \u21b3" + self.leftOp.__str__(),"  ")
        rightOp = textwrap.indent("   \u21b3" + self.rightOp.__str__(),"  ")
        return self.str + "\n " + operation + "\n " + leftOp + "\n" + rightOp + "\n"
        