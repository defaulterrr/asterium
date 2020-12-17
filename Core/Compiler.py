from Lexer import Lexer
from Parser import Parser
from Library.AddressTable import AddressTable

raw_input = """
var variable;
variable = 127;
var variable2;
variable2 = 127 * 8;
"""

input = raw_input.split(";")
sorted_expressions = []
for index in range(len(input)):
    if input[index] != "\n":
        sorted_expressions.append(input[index]+";")
print(input)
    
table = AddressTable()

lexer = Lexer().get_lexer()
outputs = []

for index in range(len(sorted_expressions)):
    expression = sorted_expressions[index]
    print("Working on: " + expression)
    tokens = lexer.lex(expression)

    pg = Parser(debug=True)
    pg.parse()
    parser = pg.getParser()
    # table.print()
    tree = parser.parse(tokens)
    tree.eval(table)
    # outputs.append(tree.generate(table))
    output = tree.generate(table)
    if output != None:
        outputs.append(output)
    print("Worked out expression: " + expression)
print("RESULT")
print("main: start 0")
for output in outputs:
    print(output)

print("_____________")
print(table.generate())