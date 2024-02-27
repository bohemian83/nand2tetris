class Parser:
    def __init__(self) -> None:
        self.lineNumber = 0
        self.endOfFile = False
        self.lines = []
        self.elements = []
        self.commands = {
            "add": "C_ARITHMETIC",
            "sub": "C_ARITHMETIC",
            "neg": "C_ARITHMETIC",
            "eq": "C_ARITHMETIC",
            "lt": "C_ARITHMETIC",
            "gt": "C_ARITHMETIC",
            "and": "C_ARITHMETIC",
            "or": "C_ARITHMETIC",
            "not": "C_ARITHMETIC",
            "push": "C_PUSH",
            "pop": "C_POP",
            "function": "C_FUNCTION",
            "call": "C_CALL",
            "label": "C_LABEL",
            "return": "C_REjTURN",
            "goto": "C_GOTO",
            "if": "C_IF",
        }

    def readFile(self, filename: str) -> None:
        with open(filename, "r") as file:
            for line in file:
                if line.strip() and line[0:2] != "//":
                    self.lines.append(line.strip())

        self.fileIterator = iter(self.lines)

    def readNextLine(self) -> str:
        self.lineNumber += 1
        if self.lineNumber == len(self.lines):
            self.endOfFile = True
        return next(self.fileIterator)

    def commandType(self, line: str):
        self.elements = line.split(" ")
        print(self.elements)
        return self.commands[self.elements[0]]

    def first_arg(self) -> str:
        if self.commands[self.elements[0]] == "C_ARITHMETIC":
            return self.elements[0]
        return self.elements[1]

    def second_arg(self) -> int:
        return int(self.elements[2])
