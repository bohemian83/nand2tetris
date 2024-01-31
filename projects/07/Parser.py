class Parser:
    def __init__(self) -> None:
        # self.filename = fileName
        self.lineNumber = 0
        self.endOfFile = False
        self.lines = []

    def readFile(self, filename):
        lines = []
        with open(filename, "r") as fl:
            for ln in fl:
                if ln.strip() and ln[0:2] != "//":
                    self.lines.append(ln.strip())

        self.fileIterator = iter(self.lines)

    def readNextLine(self):
        self.lineNumber += 1
        if self.lineNumber == len(self.lines):
            self.endOfFile = True
        return next(self.fileIterator)
