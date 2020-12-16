from Native.PrintNum import printfuncs

class ImportTable:
    def __init__(self):
        self.import_print_num = False
        self.import_print_array = False
        pass

    def enable_print_num(self):
        self.import_print_num = True

    def enable_print_array(self):
        self.import_print_array = True

    def generate(self):
        cmds = []
        if self.import_print_num:
            cmds.append(printfuncs)
        return cmds
