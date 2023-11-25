from Parser import Parser
from Decoder import Decoder
from SymbolTable import SymbolTable

filename = "F:/Projects/Coding-Raspi/nand2tetris/projects/06/max/MaxL.asm"
parser = Parser(filename)
decoder = Decoder()
SymbolTable = SymbolTable()
parser.readFile()
while not parser.endOfFile:
    line = parser.readNextLine()
    if parser.isAInstruction(line):
        print(decoder.decodeAInstruction(line))
    else:
        instruction = parser.deconstructInstruction(line)
        print(decoder.decodeCInstruction(instruction))
