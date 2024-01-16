from Parser import Parser
from Decoder import Decoder
from SymbolTable import SymbolTable

# instantiate classes and readFile iterator in parser class
input_file = "F:/Projects/Coding-Raspi/nand2tetris/projects/06/rect/Rect.asm"
parser = Parser()
parser.readFile(input_file)
decoder = Decoder()
symbols_table = SymbolTable()
symbols = symbols_table.allSymbols

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

    # check is instruction is a label and insert to the symbol table
    for line in new_lines:
        if line[0] == "(":
            symbol_key = line[line.find("(") + 1 : line.find(")")]
            symbols[symbol_key] = line_number
            # deduct one to make sure the line numbers are correct -> (labels) are not
            # included in the final program
            line_number -= 1
        line_number += 1


with open("./projects/06/assemblerOutput.hack", "w") as output_file:
    while not parser.endOfFile:
        line = parser.readNextLine()
        # if instruction is a label, skip it
        if line[0] != "(":
            # if instruction is a symbol or A-instruction, do the following:
            if parser.isSymbol(line):
                # strip line of all non alphanumeric characters.
                line = line.replace("@", "").replace("(", "").replace(")", "")
                # check if instruction is a numeric address and decode it directly.
                if parser.isInt(line):
                    output_file.write(f"{parser.decodeSymbol(int(line))}\n")
                # if instruction is in the symbol table already, get that value and decode it.
                elif line in symbols:
                    output_file.write(f"{parser.decodeSymbol(symbols[line])}\n")
                # else instruction needs to be inserted to the symbol table and decoded
                else:
                    symbols_table.insertNewValue(line)
                    output_file.write(f"{parser.decodeSymbol(symbols[line])}\n")
            # else decode is as a C-instruction
            else:
                instruction = decoder.deconstructInstruction(line)
                output_file.write(f"{decoder.decodeCInstruction(instruction)}\n")
