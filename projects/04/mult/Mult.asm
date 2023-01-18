// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

  @R0
  D=M
  @first
  M=D // Create first variable

  @R1
  D=M
  @second
  M=D // Create second variable

  @sum
  M=0 // Initialize sum = 0

  @i
  M=0 // Initialize i = 0

  @R2
  M=0 // Initialize resulting memory register to 0

(LOOP)
  @i
  D=M
  @second
  D=D-M // D = i - second
  @STOP
  D;JGE // Stop if i >= second, i.e. we added first so sum exactly second times

  @sum
  D=M
  @first
  D=D+M
  @sum
  M=D // sum = sum + first

  @i
  M=M+1 // i = i + 1
  @LOOP
  0;JMP

(STOP)
  @sum
  D=M
  @R2
  M=D
  @END
  0;JMP // R2 = sum

(END)
  @END
  0;JMP
