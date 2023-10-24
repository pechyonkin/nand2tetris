// push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 0
@SP
M = M - 1
A = M
D = M
@13
M = D
@0
D = A
@LCL
AD = D + M
@14
M = D
@13
D = M
@14
A = M
M = D
// label LOOP_START
(LOOP_START)
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
// push local 0
@0
D = A
@LCL
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
// pop local 0
@SP
M = M - 1
A = M
D = M
@13
M = D
@0
D = A
@LCL
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
// if-goto LOOP_START
@SP
M = M - 1
A = M
D = M
@LOOP_START
D;JNE
// push local 0
@0
D = A
@LCL
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
