from Parser import Parser
from CodeWriter import CodeWriter
import os, shutil  # noqa: E401


class VM_Traslator:
    def __init__(self, source) -> None:
        self.source = source

    def write_asm(self) -> None:
        # if source is not folder, use single file function,
        # else concatenate vm files into a single one, then run single file function
        if not os.path.isdir(self.source):
            input_file = self.source
            self.write_file(input_file)
        else:
            # add all vm files to list
            files = [
                os.path.join(self.source, file)
                for file in os.listdir(self.source)
                if ".vm" in file
            ]
            # check is sys.vm file exists in folder
            if "Sys.vm" in str(files):
                files.insert(0, files.pop(files.index(self.source + "/Sys.vm")))

            # concatenate content of vm files into a single one and pass it to write_file function
            with open(self.source + "/concat.vm", "wb") as wfd:
                for file in files:
                    with open(file, "rb") as fd:
                        shutil.copyfileobj(fd, wfd)
            input_file = self.source + "/concat.vm"
            self.write_file(input_file)

    def write_file(self, input_file) -> None:
        # initialise parser and codewriter
        parser = Parser()
        codewriter = CodeWriter(input_file)

        parser.readFile(input_file)

        # extract folder path and folder name for the final asm file
        folder_path = input_file[0 : input_file.rfind("/")]
        folder_name = folder_path[folder_path.rfind("/") + 1 :]

        with open(folder_path + "/" + folder_name + ".asm", "w") as output_file:
            while not parser.endOfFile:
                line = parser.readNextLine()
                commandType = parser.commandType(line)
                if commandType != "C_RETURN":
                    first_arg = parser.first_arg()
                    if commandType == "C_ARITHMETIC":
                        args = (commandType, first_arg)
                        line_to_write = codewriter.write_arithmetic(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                    elif commandType in ("C_PUSH", "C_POP", "C_CALL", "C_FUNCTION"):
                        second_arg = parser.second_arg()
                        args = (commandType, first_arg, second_arg)
                        line_to_write = codewriter.write_pushpop(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                    elif commandType in ("C_GOTO", "C_IF", "C_LABEL"):
                        args = (commandType, first_arg)
                        line_to_write = codewriter.write_branching(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                    elif commandType in ("C_CALL", "C_FUNCTION"):
                        second_arg = parser.second_arg()
                        args = (commandType, first_arg, second_arg)
                        line_to_write = codewriter.write_function_call(args)
                        output_file.write(f"//{line}\n{line_to_write}\n")
                else:
                    line_to_write = codewriter.write_return()
                    output_file.write(f"//{line}\n{line_to_write}\n")


source = "../08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
# source = "../08/FunctionCalls/FibonacciElement"
vm_translator = VM_Traslator(source)
vm_translator.write_asm()
