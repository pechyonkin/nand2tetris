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

  @8192
  D=A
  
  @n
  M=D // n = 8192 16-bit chunks to fill screen

  @i
  M=0 // to keep track of iteration
  
  @color
  M=-1 // all 1s (two's complement) to fill a chunk with black

  @SCREEN
  D=A

  @screenptr
  M=D // pointer of current screen chunk

(FILL)
  @i
  D=M

  @n
  D=D-M // i - n

  @END
  D;JGE // stop iterating if i >= n, i.e. i - n >= 0

  @color
  D=M

  @screenptr
  A=M
  M=D // dereference screen pointer

  @screenptr
  M=M+1 // increment screen pointer

  @i
  M=M+1 // increment counter

  @FILL
  0;JMP

(END)
  @END
  0;JMP


