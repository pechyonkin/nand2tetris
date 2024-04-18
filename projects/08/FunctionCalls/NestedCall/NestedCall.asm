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
// VM FILE: ../../08/FunctionCalls/NestedCall/Sys.vm
// function Sys.init 0
(Sys.init)
// push constant 4000
@4000
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 0
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5000
@5000
D = A
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
// call Sys.main 0
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
@5
D = D - A
@ARG
M = D
// CALL: goto function_name
@Sys.main
0;JMP
// CALL: declare label with return address to assembly stream
(Sys.init$ret.0)
// CALL: end of CALL handling
// pop temp 1
@SP
M = M - 1
A = M
D = M
@13
M = D
@1
D = A
@5
AD = D + A
@14
M = D
@13
D = M
@14
A = M
M = D
// label LOOP
(Sys.init$LOOP)
// goto LOOP
@Sys.init$LOOP
0;JMP
// function Sys.main 5
(Sys.main)
D = 0
@SP
A = M
M = D
@SP
M = M + 1
D = 0
@SP
A = M
M = D
@SP
M = M + 1
D = 0
@SP
A = M
M = D
@SP
M = M + 1
D = 0
@SP
A = M
M = D
@SP
M = M + 1
D = 0
@SP
A = M
M = D
@SP
M = M + 1
// push constant 4001
@4001
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 0
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5001
@5001
D = A
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
// push constant 200
@200
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 1
@SP
M = M - 1
A = M
D = M
@13
M = D
@1
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
// push constant 40
@40
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 2
@SP
M = M - 1
A = M
D = M
@13
M = D
@2
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
// push constant 6
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop local 3
@SP
M = M - 1
A = M
D = M
@13
M = D
@3
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
// push constant 123
@123
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Sys.add12 1
// CALL: push label with return address to stack
@Sys.main$ret.0
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
@Sys.add12
0;JMP
// CALL: declare label with return address to assembly stream
(Sys.main$ret.0)
// CALL: end of CALL handling
// pop temp 0
@SP
M = M - 1
A = M
D = M
@13
M = D
@0
D = A
@5
AD = D + A
@14
M = D
@13
D = M
@14
A = M
M = D
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
// push local 1
@1
D = A
@LCL
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push local 2
@2
D = A
@LCL
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push local 3
@3
D = A
@LCL
AD = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push local 4
@4
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
// function Sys.add12 0
(Sys.add12)
// push constant 4002
@4002
D = A
@SP
A = M
M = D
@SP
M = M + 1
// pop pointer 0
@SP
M = M - 1
A = M
D = M
@THIS
M = D
// push constant 5002
@5002
D = A
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
// push constant 12
@12
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
