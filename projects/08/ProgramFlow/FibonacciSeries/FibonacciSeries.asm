// push argument 1
@1
D = A
@ARG
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 1
@SP
M = M - 1
A = M
D = M
@THAT
M = D
// push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop that 0
@SP
M = M - 1
A = M
D = M
@13
M = D
@0
D = A
@THAT
AD = D + M
@14
M = D
@13
D = M
@14
A = M
M = D
// push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop that 1
@SP
M = M - 1
A = M
D = M
@13
M = D
@1
D = A
@THAT
AD = D + M
@14
M = D
@13
D = M
@14
A = M
M = D
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
// pop argument 0
@SP
M = M - 1
A = M
D = M
@13
M = D
@0
D = A
@ARG
AD = D + M
@14
M = D
@13
D = M
@14
A = M
M = D
// label MAIN_LOOP_START
(Sys.init$MAIN_LOOP_START)
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
// if-goto COMPUTE_ELEMENT
@SP
M = M - 1
A = M
D = M
@Sys.init$COMPUTE_ELEMENT
D;JNE
// goto END_PROGRAM
@Sys.init$END_PROGRAM
0;JMP
// label COMPUTE_ELEMENT
(Sys.init$COMPUTE_ELEMENT)
// push that 0
@0
D = A
@THAT
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push that 1
@1
D = A
@THAT
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
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
// pop that 2
@SP
M = M - 1
A = M
D = M
@13
M = D
@2
D = A
@THAT
AD = D + M
@14
M = D
@13
D = M
@14
A = M
M = D
// push pointer 1
@THAT
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
// pop pointer 1
@SP
M = M - 1
A = M
D = M
@THAT
M = D
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
// pop argument 0
@SP
M = M - 1
A = M
D = M
@13
M = D
@0
D = A
@ARG
AD = D + M
@14
M = D
@13
D = M
@14
A = M
M = D
// goto MAIN_LOOP_START
@Sys.init$MAIN_LOOP_START
0;JMP
// label END_PROGRAM
(Sys.init$END_PROGRAM)
