class Parser:
    def __init__(self, fileName) -> None:
        self.filename = fileName
        self.lineNumber = 0
        self.endOfFile = False
        self.lines = []

    def isSymbol(self, line):
        return line[0] == "@" or line[0] == "("

    def isInt(self, line):
        try:
            int(line)
        except ValueError:
            return False
        else:
            return True

    def decodeSymbol(self, line):
        return format(line, "016b")

    def readFile(self):
        with open(self.filename, "r") as fl:
            for ln in fl:
                if ln.strip() and ln[0:2] != "//":
                    ln = ln.strip().split(" ")[0]
                    self.lines.append(ln.strip())

        self.fileIterator = iter(self.lines)

    def readNextLine(self):
        self.lineNumber += 1
        if self.lineNumber == len(self.lines):
            self.endOfFile = True
        return next(self.fileIterator)
