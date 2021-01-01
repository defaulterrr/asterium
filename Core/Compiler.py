from Library.FunctionTable import FunctionTable
from Parser import Parser
from Library.AddressTable import AddressTable

class Compiler:
    def __init__(self):
        self._parser = Parser
        self._address_table = AddressTable()
        self._function_table = FunctionTable()

    def __parse(self):
        self._ast = self._parser.parse(self._source)

    def __eval(self):
        self._ast.eval(self._address_table,self._function_table)

    def feed(self,source):
        self._source = source
        self.__parse()
        self.__eval()

    def printast(self):
        print(self._ast)

    def printdebug(self):
        print(self._address_table)
        print(self._function_table)

compiler = Compiler()
compiler.feed('''
func test () {
    var b;
    b = 3 - 5;
}
var a;
a = 5+5;
var c;
test();
if (3>5) {
    a  = 3;
    b = 3;
}
''')
compiler.printast()
compiler.printdebug()
# compiler.feed('''
# if (3 > 5) {
#     var a;
#     a = 3 + 9;
# }
# ''')
# compiler.printast()

# compiler.feed('''
# if (3 < 5) {
#     var b;
#     b = 3 + 6;
# }
# ''')
# compiler.printast()

# compiler.feed('''
# if (3 < 5) {
#     var a;
#     a = 3+5;
# } else {
#     a =  4;
# }
# ''')
# compiler.printast()