filename = "F:/Projects/Coding-Raspi/nand2tetris/projects/06/add/Add.asm"


class Parser:
    def __init__(self, fileName):
        self.filename = fileName
        self.lineNumber = 0
        self.endOfFile = False
        self.lines = []

    def isAInstruction(self, line):
        return line[0] == "@"

    def readFile(self):
        with open(self.filename, "r") as file:
            for line in file:
                if line.strip() and line[0:2] != "//":
                    line = line.split(" ")[0]
                    self.lines.append(line.strip())

    def showLine(self, line):
        print(line)

    def readNextLine(self):
        if self.lineNumber == len(self.lines):
            self.endOfFile = True
        else:
            self.showLine(self.lines[self.lineNumber])
            self.lineNumber += 1


parser = Parser(filename)
parser.readFile()
while not parser.endOfFile:
    parser.readNextLine()
