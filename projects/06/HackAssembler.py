from Parser import Parser
from Decoder import Decoder
from SymbolTable import SymbolTable

filename = "F:/Projects/Coding-Raspi/nand2tetris/projects/06/max/MaxL.asm"
parser = Parser(filename)
decoder = Decoder()
SymbolTable = SymbolTable()
parser.readFile()
file = open("./projects/06/assemblerOutput.hack", "w")
with open("./projects/06/assemblerOutput.hack", "a") as file:
    while not parser.endOfFile:
        line = parser.readNextLine()
        if parser.isAInstruction(line):
            print(f"{line, decoder.decodeAInstruction(line)}")
            file.write(f"{decoder.decodeAInstruction(line)}\n")
        else:
            instruction = parser.deconstructInstruction(line)
            file.write(f"{decoder.decodeCInstruction(instruction)}\n")
            print(f"{line, decoder.decodeCInstruction(instruction)}")
