from Library.FunctionTable import FunctionTable
from Lexer import Lexer
from Parser import Parser
from Library.AddressTable import AddressTable

raw_input = """
var variable;
variable = 127;
var variable2;
variable2 = 127 * 8;
"""

raw_input2 = """
var a;
var b;
a = 3+3;
b = 6+8/4;
"""

# input = raw_input.split(";")
sorted_expressions = []
# for index in range(len(input)):
#     if input[index] != "\n":
#         sorted_expressions.append(input[index]+";")
# print(input)
sorted_expressions.append(raw_input2)

atable = AddressTable()
ftable = FunctionTable()

lexer = Lexer().get_lexer()
outputs = []

for index in range(len(sorted_expressions)):
    expression = sorted_expressions[index]
    print("Working on: " + expression)
    tokens = lexer.lex(expression)
    # for token in tokens:
    #     print(token)
    pg = Parser(debug=True)
    pg.parse()
    parser = pg.getParser()
    # table.print()
    tree = parser.parse(tokens)
    tree.eval(atable, ftable)
    # outputs.append(tree.generate(table))
    output = tree.generate(atable, ftable)
    if output != None:
        outputs.append(output)
    print("Worked out expression: " + expression)
print("RESULT")
print("main: start 0")
for output in outputs:
    print(output)

print("_____________")
print(atable.generate())
print(ftable.generate(atable,ftable))
