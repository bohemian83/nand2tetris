class CodeWriter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.jumper = 0

    def write_arithmetic(self, args):
        command = args[1]

        match command:
            case "add":
                return "@SP\nA=M-1\nD=M\n@R13\nM=D\n@SP\nA=M-1\nA=A-1\nD=M\n@R13\nD=D+M\n@SP\nM=M-1\nM=M-1\nA=M\nM=D\n@SP\nM=M+1"
            case "sub":
                return "@SP\nA=M-1\nD=M\n@R13\nM=D\n@SP\nA=M-1\nA=A-1\nD=M\n@R13\nD=D-M\n@SP\nM=M-1\nM=M-1\nA=M\nM=D\n@SP\nM=M+1"
            case "neg":
                return "@SP\nA=M-1\nD=M\n@R13\nM=-D\nD=M\n@SP\nA=M-1\nM=D\n"  # "@SP\nM=M+1"
            case "eq":
                self.jumper += 1
                return (
                    "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@JS_"
                    + str(self.jumper)
                    + "\nD;JEQ\n@SP\nA=M-1\nM=0\n@JE_"
                    + str(self.jumper)
                    + "\n0;JMP\n(JS_"
                    + str(self.jumper)
                    + ")\n@SP\nA=M-1\nM=-1\n(JE_"
                    + str(self.jumper)
                    + ")"
                )
            case "gt":
                self.jumper += 1
                return (
                    "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@JS_"
                    + str(self.jumper)
                    + "\nD;JGT\n@SP\nA=M-1\nM=0\n@JE_"
                    + str(self.jumper)
                    + "\n0;JMP\n(JS_"
                    + str(self.jumper)
                    + ")\n@SP\nA=M-1\nM=-1\n(JE_"
                    + str(self.jumper)
                    + ")"
                )
            case "lt":
                self.jumper += 1
                return (
                    "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@JS_"
                    + str(self.jumper)
                    + "\nD;JLT\n@SP\nA=M-1\nM=0\n@JE_"
                    + str(self.jumper)
                    + "\n0;JMP\n(JS_"
                    + str(self.jumper)
                    + ")\n@SP\nA=M-1\nM=-1\n(JE_"
                    + str(self.jumper)
                    + ")"
                )
            case "and":
                return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M\n@SP\nM=M+1"
            case "or":
                return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M\n@SP\nM=M+1"
            case "not":
                return "@SP\nM=M-1\nA=M\nD=M\nD=!D\n@SP\nA=M\nM=D\n@SP\nM=M+1"
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
                    if index == 0:
                        return "@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                    if index == 1:
                        return "@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1"
                if command == "C_POP":
                    if index == 0:
                        return "@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D"
                    if index == 1:
                        return "@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D"

    def write_branching(self, args):
        command, label = args[0], args[1]

        match command:
            case "C_LABEL":
                return f"({label})"
            case "C_GOTO":
                return f"@{label}\n0;JMP"
            case "C_IF":
                return f"@SP\nM=M-1\nA=M\nD=M\n@{label}\nD;JNE"
