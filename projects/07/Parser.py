class Parser:
    def __init__(self) -> None:
        # self.filename = fileName
        self.lineNumber = 0
        self.endOfFile = False
        self.lines = []

    def readFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                if line.strip() and line[0:2] != "//":
                    self.lines.append(line.strip())

        self.fileIterator = iter(self.lines)

    def readNextLine(self):
        self.lineNumber += 1
        if self.lineNumber == len(self.lines):
            self.endOfFile = True
        return next(self.fileIterator)
