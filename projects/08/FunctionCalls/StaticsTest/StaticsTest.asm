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
// VM FILE: ../../08/FunctionCalls/StaticsTest/Class1.vm
// function Class1.set 0
(Class1.set)
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
// pop static 0
@SP
M = M - 1
A = M
D = M
@Class1.0
M = D
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
// pop static 1
@SP
M = M - 1
A = M
D = M
@Class1.1
M = D
// push constant 0
@0
D = A
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
// function Class1.get 0
(Class1.get)
// push static 0
@Class1.0
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push static 1
@Class1.1
D = M
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
// VM FILE: ../../08/FunctionCalls/StaticsTest/Sys.vm
// function Sys.init 0
(Sys.init)
// push constant 6
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 8
@8
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Class1.set 2
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
@7
D = D - A
@ARG
M = D
// CALL: goto function_name
@Class1.set
0;JMP
// CALL: declare label with return address to assembly stream
(Sys.init$ret.0)
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
// push constant 23
@23
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 15
@15
D = A
@SP
A = M
M = D
@SP
M = M + 1
// call Class2.set 2
// CALL: push label with return address to stack
@Sys.init$ret.1
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
@7
D = D - A
@ARG
M = D
// CALL: goto function_name
@Class2.set
0;JMP
// CALL: declare label with return address to assembly stream
(Sys.init$ret.1)
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
// call Class1.get 0
// CALL: push label with return address to stack
@Sys.init$ret.2
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
@Class1.get
0;JMP
// CALL: declare label with return address to assembly stream
(Sys.init$ret.2)
// CALL: end of CALL handling
// call Class2.get 0
// CALL: push label with return address to stack
@Sys.init$ret.3
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
@Class2.get
0;JMP
// CALL: declare label with return address to assembly stream
(Sys.init$ret.3)
// CALL: end of CALL handling
// label WHILE
(Sys.init$WHILE)
// goto WHILE
@Sys.init$WHILE
0;JMP
// VM FILE: ../../08/FunctionCalls/StaticsTest/Class2.vm
// function Class2.set 0
(Class2.set)
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
// pop static 0
@SP
M = M - 1
A = M
D = M
@Class2.0
M = D
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
// pop static 1
@SP
M = M - 1
A = M
D = M
@Class2.1
M = D
// push constant 0
@0
D = A
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
// function Class2.get 0
(Class2.get)
// push static 0
@Class2.0
D = M
@SP
A = M
M = D
@SP
M = M + 1
// push static 1
@Class2.1
D = M
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
