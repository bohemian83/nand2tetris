from Parser import Parser
from CodeWriter import CodeWriter

# instantiate classes and readFile iterator in parser class
# input_file = "./StackArithmetic/StackTest/StackTest.vm"
input_file = "../08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
# input_file = "../08/ProgramFlow/BasicLoop/BasicLoop.vm"
file_name = input_file[input_file.rfind("/") + 1 : -3]
folder_name = input_file[0 : input_file.rfind("/")]
parser = Parser()
parser.readFile(input_file)
codewriter = CodeWriter(file_name)

# read in and format file
with open(input_file, "r") as input:
    lines = input.readlines()
    new_lines = []
    line_number = 0
    # remove comments, empty lines and spaces before instructions
    for line in lines:
        if line.strip() and line[0:2] != "//":
            line = line.strip().split(" ")[0]
            new_lines.append(line.strip())


with open(folder_name + "/" + file_name + ".asm", "w") as output_file:
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
