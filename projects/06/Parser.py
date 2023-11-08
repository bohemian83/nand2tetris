import re


class Parser:
    def __init__(self, fileName):
        self.filename = fileName
        self.lineNumber = 0
        self.endOfFile = False
        self.lines = []
        self.dest = ""
        self.comp = ""
        self.jump = ""

    def isAInstruction(self, line):
        return line[0] == "@"

    def readFile(self):
        with open(self.filename, "r") as file:
            for line in file:
                if line.strip() and line[0:2] != "//":
                    line = line.split(" ")[0]
                    self.lines.append(line.strip())

        self.fileIterator = iter(self.lines)

    def readNextLine(self):
        self.lineNumber += 1
        if self.lineNumber == len(self.lines):
            self.endOfFile = True
        return next(self.fileIterator)

    def deconstruct_instruction(self, instruction):
        self.dest, self.comp, self.jump = "", "", ""

        if self.isAInstruction(instruction):
            instr = bin(int(instruction[1:]))
            return instr

        if re.match("\w+=\w([\+\-\|\&])?\w?", instruction):
            self.dest = re.split("=", instruction)[0]
            self.comp = re.split("=", instruction)[1]

        if re.match("\w+;\w+", instruction):
            self.comp = re.split(";", instruction)[0]
            self.jump = re.split(";", instruction)[1]

        return [self.dest, self.comp, self.jump]


filename = "F:/Projects/Coding-Raspi/nand2tetris/projects/06/max/MaxL.asm"
parser = Parser(filename)
parser.readFile()
while not parser.endOfFile:
    line = parser.readNextLine()
    print(parser.deconstruct_instruction(line))
