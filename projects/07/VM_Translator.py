from Parser import Parser
from CodeWriter import CodeWriter
import os


class VM_Traslator:
    def __init__(self, source) -> None:
        self.source = source

    def write_asm(self) -> None:

        # if source is folder, adjust path
        folder_path = (
            self.source
            if os.path.isdir(self.source)
            else self.source[0 : self.source.rfind("/")]
        )
        folder_name = folder_path[folder_path.rfind("/") + 1 :]

        with open(folder_path + "/" + folder_name + ".asm", "w") as output:
            if os.path.isdir(self.source):
                # If source is a directory, process each text file within it
                files = [
                    os.path.join(self.source, file)
                    for file in os.listdir(self.source)
                    if ".vm" in file
                ]

                # check is sys.vm file exists in folder and place it first in the list
                if "Sys.vm" in str(files):
                    files.insert(0, files.pop(files.index(self.source + "/Sys.vm")))

                # write each translated file to output
                for file_name in files:
                    self.write_file(file_name, output)

            elif os.path.isfile(self.source):
                # If source is a single text file
                self.write_file(self.source, output)

    def write_file(self, input, output) -> None:
        # initialise parser and codewriter and have file read by parser
        parser = Parser()
        codewriter = CodeWriter(input)
        parser.readFile(input)
        line_to_write = ""

        while not parser.endOfFile:

            line = parser.readNextLine()
            commandType = parser.commandType(line)

            if commandType != "C_RETURN":
                if commandType == "C_ARITHMETIC":
                    line_to_write = codewriter.write_arithmetic(
                        (commandType, parser.first_arg())
                    )
                elif commandType in ("C_PUSH", "C_POP"):
                    line_to_write = codewriter.write_pushpop(
                        (commandType, parser.first_arg(), parser.second_arg())
                    )
                elif commandType in ("C_GOTO", "C_IF", "C_LABEL"):
                    line_to_write = codewriter.write_branching(
                        (commandType, parser.first_arg())
                    )
                elif commandType == "C_FUNCTION":
                    line_to_write = codewriter.write_function(
                        (commandType, parser.first_arg(), parser.second_arg())
                    )
                elif commandType == "C_CALL":
                    line_to_write = codewriter.write_call(
                        (commandType, parser.first_arg(), parser.second_arg())
                    )
            else:
                line_to_write = codewriter.write_return()

            output.write(f"//{line}\n{line_to_write}\n")


# source = "../08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
source = "../08/FunctionCalls/FibonacciElement"
vm_translator = VM_Traslator(source)
vm_translator.write_asm()
