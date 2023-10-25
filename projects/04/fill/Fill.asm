// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
//pseudocode
//max=8191
//loop
//i=0
//if kdb=0 goto black
// else goto clear
//goto loop
//black
//screen = 16384
//screen + i = -1
//i = i + 16
//if i < max go to black
//else goto loop


@8192
D=A
@max
M=D

(LOOP)
@i
M=0

@KBD
D=M

@BLACK
D;JGT

@CLEAR
0;JMP

@LOOP
0;JMP

(BLACK)
@SCREEN
D=A

@i
A=D+M
M=-1

@i
M=M+1

@max
D=M
@i
D=M-D

@BLACK
D;JLT

@LOOP
0;JMP


(CLEAR)
@SCREEN
D=A

@i
A=D+M
M=0

@i
M=M+1

@max
D=M

@i
D=M-D

@CLEAR
D;JLT

@LOOP
0;JMP



