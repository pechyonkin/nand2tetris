@256
D = A
@SP
M = D
// CALL: push label with return address to stack
@BOOTSTRAP$ret.-1
D = A
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save LCL to stack
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save ARG to stack
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THIS to stack
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THAT to stack
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: LCL = SP
@SP
D = M
@LCL
M = D
// CALL: reposition ARG
@5
D = D - A
@ARG
M = D
// CALL: goto function_name
@Sys.init
0;JMP
// CALL: declare label with return address to assembly stream
(BOOTSTRAP$ret.-1)
// CALL: end of CALL handling
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
// CALL: push label with return address to stack
@Main.fibonacci$ret.0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save LCL to stack
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save ARG to stack
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THIS to stack
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THAT to stack
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: LCL = SP
@SP
D = M
@LCL
M = D
// CALL: reposition ARG
@6
D = D - A
@ARG
M = D
// CALL: goto function_name
@Main.fibonacci
0;JMP
// CALL: declare label with return address to assembly stream
(Main.fibonacci$ret.0)
// CALL: end of CALL handling
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
// CALL: push label with return address to stack
@Main.fibonacci$ret.1
D = A
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save LCL to stack
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save ARG to stack
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THIS to stack
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THAT to stack
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: LCL = SP
@SP
D = M
@LCL
M = D
// CALL: reposition ARG
@6
D = D - A
@ARG
M = D
// CALL: goto function_name
@Main.fibonacci
0;JMP
// CALL: declare label with return address to assembly stream
(Main.fibonacci$ret.1)
// CALL: end of CALL handling
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
// CALL: push label with return address to stack
@Sys.init$ret.0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save LCL to stack
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save ARG to stack
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THIS to stack
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: save THAT to stack
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1
// CALL: LCL = SP
@SP
D = M
@LCL
M = D
// CALL: reposition ARG
@6
D = D - A
@ARG
M = D
// CALL: goto function_name
@Main.fibonacci
0;JMP
// CALL: declare label with return address to assembly stream
(Sys.init$ret.0)
// CALL: end of CALL handling
// label WHILE
(Sys.init$WHILE)
// goto WHILE
@Sys.init$WHILE
0;JMP
