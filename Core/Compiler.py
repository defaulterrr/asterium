from Library.FunctionTable import FunctionTable
from YaccParser import Parser
from Library.AddressTable import AddressTable

result = Parser.parse('''
var a;
a = 3 + 5;
''')

print(result)