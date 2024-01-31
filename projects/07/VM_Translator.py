from Parser import Parser
from CodeWriter import CodeWriter

# instantiate classes and readFile iterator in parser class
input_file = "F:/Projects/Coding-Raspi/nand2tetris/projects/07/MemoryAccess/BasicTest/BasicTest.vm"
parser = Parser()
parser.readFile(input_file)
codewriter = CodeWriter()

# populate symbol table with labels
with open(input_file, "r") as input:
    lines = input.readlines()
    new_lines = []
    line_number = 0
    # remove comments, empty lines and spaces before instructions
    for line in lines:
        if line.strip() and line[0:2] != "//":
            line = line.strip().split(" ")[0]
            new_lines.append(line.strip())


with open(
    "F:/Projects/Coding-Raspi/nand2tetris/projects/07/BasicTest.asm", "w"
) as output_file:
    while not parser.endOfFile:
        line = parser.readNextLine()
        # if instruction is a label, skip it
        output_file.write(f"{line}\n")
