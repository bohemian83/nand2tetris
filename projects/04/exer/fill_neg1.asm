//Set first n entries
//of the memory block beginning in address base to -1
//Inputs R0: base, R1:n
//pseudocode
//base=R0
//n=R1
//i=1
//if i>R1 goto STOP
//RAM[base] = -1
//i=i+1
//base = base + 1
//goto LOOP
//STOP
//END

//@R0
//D=M
//@base
//M=D

//@R1
//D=M
//@n
//M=D

@i
M=0

(LOOP)
@i
D=M
@R1
D=D-M
@END
D;JEQ

@R0
D=M
@i
A=D+M
M=-1
@i
M=M+1

@LOOP
0;JMP

(END)
@END
0;JMP


