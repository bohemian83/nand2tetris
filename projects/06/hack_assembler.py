from Parser import Parser
from Decoder import Decoder
from SymbolTable import SymbolTable

FILENAME = "./max/MaxL.asm"
parser = Parser(FILENAME)
decoder = Decoder()
SymbolTable = SymbolTable()
parser.read_file()
while not parser.end_of_file:
    line = parser.read_next_line()
    if parser.is_a_instruction(line):
        print(decoder.decode_c_instruction(line))
    else:
        instruction = parser.deconstruct_instruction(line)
        print(decoder.decode_c_instruction(instruction))
