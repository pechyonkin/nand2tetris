@256
D = A
@SP
M = D
@BOOTSTRAP$ret.-1
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@LCL
M = D
@5
D = D - A
@ARG
M = D
@Sys.init
0;JMP
(BOOTSTRAP$ret.-1)
// Bootstrap complete
// VM FILE: ../../08/FunctionCalls/FibonacciElement/Main.vm
// function Main.fibonacci 0
(Main.fibonacci)
// push argument 0
@0
D = A
@ARG
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push constant 2
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1
// lt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUE_THEN_JUMP.Main.3
D; JLT
D = 0
@FALSE_THEN_DONT_JUMP.Main.3
0; JMP
(TRUE_THEN_JUMP.Main.3)
D = -1
(FALSE_THEN_DONT_JUMP.Main.3)
@SP
A = M
M = D
@SP
M = M + 1
// if-goto IF_TRUE
@SP
M = M - 1
A = M
D = M
@Main.fibonacci$IF_TRUE
D;JNE
// goto IF_FALSE
@Main.fibonacci$IF_FALSE
0;JMP
// label IF_TRUE
(Main.fibonacci$IF_TRUE)
// push argument 0
@0
D = A
@ARG
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// return
@LCL
D = M
@R13
M = D
@R13
D = M
@5
D = D - A
A = D
D = M
@R14
M = D
@SP
M = M - 1
A = M
D = M
@ARG
A = M
M = D
@ARG
D = M
@SP
M = D + 1
@R13
D = M
@1
D = D - A
A = D
D = M
@THAT
M = D
@R13
D = M
@2
D = D - A
A = D
D = M
@THIS
M = D
@R13
D = M
@3
D = D - A
A = D
D = M
@ARG
M = D
@R13
D = M
@4
D = D - A
A = D
D = M
@LCL
M = D
@R14
A = M
0;JMP
// label IF_FALSE
(Main.fibonacci$IF_FALSE)
// push argument 0
@0
D = A
@ARG
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push constant 2
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1
// sub
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@SP
A = M
M = D
@SP
M = M + 1
// call Main.fibonacci 1
@Main.fibonacci$ret.0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@LCL
M = D
@6
D = D - A
@ARG
M = D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.0)
// push argument 0
@0
D = A
@ARG
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1
// sub
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@SP
A = M
M = D
@SP
M = M + 1
// call Main.fibonacci 1
@Main.fibonacci$ret.1
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@LCL
M = D
@6
D = D - A
@ARG
M = D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)
// add
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M + D
@SP
A = M
M = D
@SP
M = M + 1
// return
@LCL
D = M
@R13
M = D
@R13
D = M
@5
D = D - A
A = D
D = M
@R14
M = D
@SP
M = M - 1
A = M
D = M
@ARG
A = M
M = D
@ARG
D = M
@SP
M = D + 1
@R13
D = M
@1
D = D - A
A = D
D = M
@THAT
M = D
@R13
D = M
@2
D = D - A
A = D
D = M
@THIS
M = D
@R13
D = M
@3
D = D - A
A = D
D = M
@ARG
M = D
@R13
D = M
@4
D = D - A
A = D
D = M
@LCL
M = D
@R14
A = M
0;JMP
// VM FILE: ../../08/FunctionCalls/FibonacciElement/Sys.vm
// function Sys.init 0
(Sys.init)
// push constant 4
@4
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Main.fibonacci 1
@Sys.init$ret.0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@LCL
M = D
@6
D = D - A
@ARG
M = D
@Main.fibonacci
0;JMP
(Sys.init$ret.0)
// label WHILE
(Sys.init$WHILE)
// goto WHILE
@Sys.init$WHILE
0;JMP
