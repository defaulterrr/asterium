from rply.token import BaseBox

class BinaryOperation(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right