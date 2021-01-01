class Node:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        # print(self)

    def eval(self, atable, ftable):
        # print("Node eval")
        # print(self.left,self.right)
        self.left.eval(atable,ftable)
        self.right.eval(atable,ftable)

    def __str__(self):
        # import traceback
        # traceback.print_stack()
        import textwrap
        self.str = "Node *"
        self.leftstr = textwrap.indent("   \u21b3" + self.left.__str__(),"  ")
        self.rightstr = textwrap.indent("   \u21b3" + self.right.__str__(),"  ")
        return self.str + "\n " + self.leftstr + "\n " + self.rightstr + "\n "

    def generate(self,atable,ftable):
        cmds = []
        cmds.append(self.left.generate(atable,ftable))
        cmds.append(self.right.generate(atable,ftable))
        finalcmds = [x for x in cmds if x != None]
        # print("Node cmds")
        # print(finalcmds)
        return "".join(finalcmds)