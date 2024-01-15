import re


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

        self.fileIterator = iter(self.lines)

    def readNextLine(self):
        self.lineNumber += 1
        if self.lineNumber == len(self.lines):
            self.endOfFile = True
        return next(self.fileIterator)

    def deconstructInstruction(self, instruction):
        dest, comp, jump = "", "", ""

        if re.match("\w+=\w([\+\-\|\&])?\w?", instruction):
            dest = re.split("=", instruction)[0]
            comp = re.split("=", instruction)[1]

        if re.match("\w+;\w+", instruction):
            comp = re.split(";", instruction)[0]
            jump = re.split(";", instruction)[1]
        return [dest, comp, jump]
