from lark import Lark, tree
from pathlib import Path

GRAMMAR_FILE = r'STark.lark'
SOURCE_FILES = r'tests'

with open(GRAMMAR_FILE, 'rt') as file:
    grammar = file.read()

TXT_FILE = r'exports\AST_export.txt'
testcases = Path(SOURCE_FILES).rglob('*.st')

if __name__ == '__main__':
    parser = Lark(grammar, maybe_placeholders=False, keep_all_tokens=False)

    txt_export = open(TXT_FILE, "w")
    for testcase in testcases:
        with open(testcase, 'rt') as file:
            source = file.read()
            #print(str(testcase))
            ast = parser.parse(source)
            #print(ast)
            #txt_export.write(str(ast.pretty()))
            txt_export.write(str(ast))
            tree.pydot__tree_to_dot(parser.parse(source), 'exports' / testcase)