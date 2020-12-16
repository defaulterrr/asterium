from rply.token import BaseBox

class UnaryOperation(BaseBox):
    def __init__(self,call):
        self.call = call