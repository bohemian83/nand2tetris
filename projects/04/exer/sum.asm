// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

//// Program: Sum1ToN (R0 represents N)
// Computes R1 = 1 + 2 + 3 + ... + R0
// Usage: put a value >= 1 in R0
//i = 1
//sum = 0
//LOOP:
//if (i > R0) goto STOP
//sum = sum + i
//i = i + 1
//goto LOOP
//STOP:
//R1 = sum

//i=1
@i
M=1

//sum=0
@sum
M=0

//if (i>R0) goto STOP
(LOOP)
@i
D=M
@R0
D=D-M
@STOP
D;JGT

//sum = sum + i
@sum
D=M
@i
D=D+M
@sum
M=D

//i = i + 1
@i
M=M+1

//goto LOOP
@LOOP
0;JMP

(STOP)
//R1=sum
@sum
M=M+1
D=M
@R1
M=D

//infinite loop
(END)
@END
0;JMP
