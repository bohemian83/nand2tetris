from Parser import Parser
from CodeWriter import CodeWriter
import os


class VM_Traslator:
    def __init__(self, source) -> None:
        self.source = "../08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
        # instantiate classes and readFile iterator in parser class
        self.is_dir = os.path.isdir(self.source)
        self.file_name = self.source[self.source.rfind("/") + 1 : -3]
        self.folder_path = self.source[0 : self.source.rfind("/")]
        self.folder_name = self.folder_path[self.folder_path.rfind("/") + 1 :]
        self.parser = Parser()
        self.codewriter = CodeWriter(self.source)

    def read_file(self):
        # read in and format file
        self.parser.readFile(self.source)
        with open(self.source, "r") as input:
            lines = input.readlines()
            new_lines = []
            # remove comments, empty lines and spaces before instructions
            for line in lines:
                if line.strip() and line[0:2] != "//":
                    line = line.strip().split(" ")[0]
                    new_lines.append(line.strip())

        return new_lines

    def write_file(self) -> None:
        with open(
            self.folder_path + "/" + self.folder_name + ".asm", "w"
        ) as output_file:
            while not self.parser.endOfFile:
                line = self.parser.readNextLine()
                commandType = self.parser.commandType(line)
                if commandType != "C_RETURN":
                    first_arg = self.parser.first_arg()
                    if commandType == "C_ARITHMETIC":
                        args = (commandType, first_arg)
                        line_to_write = self.codewriter.write_arithmetic(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                    elif commandType in ("C_PUSH", "C_POP", "C_CALL", "C_FUNCTION"):
                        second_arg = self.parser.second_arg()
                        args = (commandType, first_arg, second_arg)
                        line_to_write = self.codewriter.write_pushpop(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                    elif commandType in ("C_GOTO", "C_IF", "C_LABEL"):
                        args = (commandType, first_arg)
                        line_to_write = self.codewriter.write_branching(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                    elif commandType in ("C_CALL", "C_FUNCTION"):
                        second_arg = self.parser.second_arg()
                        args = (commandType, first_arg, second_arg)
                        line_to_write = self.codewriter.write_function_call(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                else:
                    line_to_write = self.codewriter.write_return()
                    output_file.write(f"//{line}\n{line_to_write}\n")


vm_translator = VM_Traslator("source")
vm_translator.read_file()
vm_translator.write_file()
