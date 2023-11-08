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
        if not self.isAInstruction(instruction):
            print(instruction)


filename = "F:/Projects/Coding-Raspi/nand2tetris/projects/06/max/MaxL.asm"
parser = Parser(filename)
parser.readFile()
while not parser.endOfFile:
    line = parser.readNextLine()
    parser.deconstruct_instruction(line)
