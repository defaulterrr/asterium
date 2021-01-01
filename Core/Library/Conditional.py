class Conditional:
    def __init__(self,comparison,true_block,false_block=None):
        self.comparison = comparison
        self.true_block = true_block
        if false_block == None:
            self.is_else_present = False
        else: 
            self.is_else_present = True
            self.false_block = false_block
        
    def __str__(self):
        import textwrap
        self.str = "If *"
        comparison = textwrap.indent("   \u21b3" + self.comparison.__str__(),"  ")
        leftstr = textwrap.indent("   \u21b3" + self.true_block.__str__(),"  ")
        if self.is_else_present:
            rightstr = textwrap.indent("   \u21b3" + self.false_block.__str__(),"  ")
            return self.str + "\n " + comparison + '\n' + leftstr + "\n " + rightstr + "\n "
        return self.str + "\n " + comparison + '\n' + leftstr + "\n "
        print(self.true_block.__str__())
            
        