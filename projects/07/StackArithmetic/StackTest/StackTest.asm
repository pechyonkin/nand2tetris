// push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// eq
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUE_THEN_JUMP.StackTest.2
D; JEQ
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.2
0; JMP
(TRUE_THEN_JUMP.StackTest.2)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.2)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 16
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
// eq
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUE_THEN_JUMP.StackTest.5
D; JEQ
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.5
0; JMP
(TRUE_THEN_JUMP.StackTest.5)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.5)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 16
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
// eq
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUE_THEN_JUMP.StackTest.8
D; JEQ
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.8
0; JMP
(TRUE_THEN_JUMP.StackTest.8)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.8)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 892
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 891
@891
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
@TRUE_THEN_JUMP.StackTest.11
D; JLT
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.11
0; JMP
(TRUE_THEN_JUMP.StackTest.11)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.11)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 892
@892
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
@TRUE_THEN_JUMP.StackTest.14
D; JLT
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.14
0; JMP
(TRUE_THEN_JUMP.StackTest.14)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.14)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 891
@891
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
@TRUE_THEN_JUMP.StackTest.17
D; JLT
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.17
0; JMP
(TRUE_THEN_JUMP.StackTest.17)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.17)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32767
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// gt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUE_THEN_JUMP.StackTest.20
D; JGT
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.20
0; JMP
(TRUE_THEN_JUMP.StackTest.20)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.20)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32767
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
// gt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUE_THEN_JUMP.StackTest.23
D; JGT
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.23
0; JMP
(TRUE_THEN_JUMP.StackTest.23)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.23)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1
// gt
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M - D
@TRUE_THEN_JUMP.StackTest.26
D; JGT
D = 0
@FALSE_THEN_DONT_JUMP.StackTest.26
0; JMP
(TRUE_THEN_JUMP.StackTest.26)
D = -1
(FALSE_THEN_DONT_JUMP.StackTest.26)
@SP
A = M
M = D
@SP
M = M + 1
// push constant 57
@57
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 31
@31
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push constant 53
@53
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
// push constant 112
@112
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
// neg
@SP
M = M - 1
A = M
D = M
D = - D
@SP
A = M
M = D
@SP
M = M + 1
// and
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M & D
@SP
A = M
M = D
@SP
M = M + 1
// push constant 82
@82
D = A
@SP
A = M
M = D
@SP
M = M + 1
// or
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
D = M | D
@SP
A = M
M = D
@SP
M = M + 1
// not
@SP
M = M - 1
A = M
D = M
D = ! D
@SP
A = M
M = D
@SP
M = M + 1
