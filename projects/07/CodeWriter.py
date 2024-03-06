class CodeWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_arithmetic(self, args):
        return args

    def write_pushpop(self, args):

        command, segment, index = args[0], args[1], args[2]

        match segment:
            case "constant":
                # only push command for constant segment
                return f"@{index}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1"
            case "local":
                if command == "C_PUSH":
                    return f"@{index}\nD=A\n@LCL\nD=D+M\n@R13\nM=D\n@R13\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                if command == "C_POP":
                    return f"@{index}\nD=A\n@LCL\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\n@SP\nA=M\nD=M\n@R13\nA=M\nM=D"
            case "argument":
                if command == "C_PUSH":
                    return f"@{index}\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@R13\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                if command == "C_POP":
                    return f"@{index}\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\n@SP\nA=M\nD=M\n@R13\nA=M\nM=D"
            case "this":
                if command == "C_PUSH":
                    return f"@{index}\nD=A\n@THIS\nD=D+M\n@R13\nM=D\n@R13\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                if command == "C_POP":
                    return f"@{index}\nD=A\n@THIS\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\n@SP\nA=M\nD=M\n@R13\nA=M\nM=D"
            case "that":
                if command == "C_PUSH":
                    return f"@{index}\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@R13\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                if command == "C_POP":
                    return f"@{index}\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\n@SP\nA=M\nD=M\n@R13\nA=M\nM=D"
            case "static":
                label = self.file_name + "." + str(index)
                if command == "C_PUSH":
                    return f"@{label}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                if command == "C_POP":
                    return f"@SP\nM=M-1\nA=M\nD=M\n@{label}\nM=D"
            case "temp":
                if command == "C_PUSH":
                    return f"@R{index+5}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                if command == "C_POP":
                    return f"@SP\nM=M-1\nA=M\nD=M\n@R{index+5}\nM=D"
            case "pointer":
                if command == "C_PUSH":
                    pass
                if command == "C_POP":
                    pass
