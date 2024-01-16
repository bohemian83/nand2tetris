from Parser import Parser
from Decoder import Decoder
from SymbolTable import SymbolTable

# instantiate classes
input_file = "F:/Projects/Coding-Raspi/nand2tetris/projects/06/max/Max.asm"
parser = Parser(input_file)
parser.readFile()
decoder = Decoder()
symbols_table = SymbolTable()
symbols = symbols_table.allSymbols

# populate symbol table with labels
with open(input_file, "r") as input:
    lines = input.readlines()
    new_lines = []
    line_number = 0
    for line in lines:
        if line.strip() and line[0:2] != "//":
            line = line.strip().split(" ")[0]
            new_lines.append(line.strip())

    for line in new_lines:
        if line[0] == "(":
            symbol_key = line[line.find("(") + 1 : line.find(")")]
            symbols[symbol_key] = line_number
        line_number += 1


with open("./projects/06/assemblerOutput.hack", "a") as output_file:
    while not parser.endOfFile:
        line = parser.readNextLine()
        if parser.isSymbol(line):
            line = line.replace("@", "").replace("(", "").replace(")", "")
            if parser.isInt(line):
                print(line, parser.decodeSymbol(int(line)))
                output_file.write(f"{parser.decodeSymbol(int(line))}\n")
            elif line in symbols:
                print(line, parser.decodeSymbol(symbols[line]))
                output_file.write(f"{parser.decodeSymbol(symbols[line])}\n")
            else:
                symbols_table.insertNewValue(line)
                print(line, parser.decodeSymbol(symbols[line]))
                output_file.write(f"{parser.decodeSymbol(symbols[line])}\n")
        else:
            instruction = decoder.deconstructInstruction(line)
            output_file.write(f"{decoder.decodeCInstruction(instruction)}\n")
            print(f"{line, decoder.decodeCInstruction(instruction)}")
