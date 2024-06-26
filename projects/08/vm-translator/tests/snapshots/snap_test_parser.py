# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_eq 1'] = [
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M - D',
    '@TRUE_THEN_JUMP.Foo.0',
    'D; JEQ',
    'D = 0',
    '@FALSE_THEN_DONT_JUMP.Foo.0',
    '0; JMP',
    '(TRUE_THEN_JUMP.Foo.0)',
    'D = -1',
    '(FALSE_THEN_DONT_JUMP.Foo.0)',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_function_op 1'] = [
    '(SimpleFunction.test)',
    'D = 0',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    'D = 0',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_label_ops[path0] 1'] = [
    '// push constant 0',
    '@0',
    'D = A',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop local 0',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@0',
    'D = A',
    '@LCL',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// label LOOP_START',
    '(Sys.init$LOOP_START)',
    '// push argument 0',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// push local 0',
    '@0',
    'D = A',
    '@LCL',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// add',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M + D',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop local 0',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@0',
    'D = A',
    '@LCL',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// push argument 0',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// push constant 1',
    '@1',
    'D = A',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// sub',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M - D',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop argument 0',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// push argument 0',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// if-goto LOOP_START',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@Sys.init$LOOP_START',
    'D;JNE',
    '// push local 0',
    '@0',
    'D = A',
    '@LCL',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_label_ops[path1] 1'] = [
    '// push argument 1',
    '@1',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop pointer 1',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@THAT',
    'M = D',
    '// push constant 0',
    '@0',
    'D = A',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop that 0',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@0',
    'D = A',
    '@THAT',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// push constant 1',
    '@1',
    'D = A',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop that 1',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@1',
    'D = A',
    '@THAT',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// push argument 0',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// push constant 2',
    '@2',
    'D = A',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// sub',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M - D',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop argument 0',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// label MAIN_LOOP_START',
    '(Sys.init$MAIN_LOOP_START)',
    '// push argument 0',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// if-goto COMPUTE_ELEMENT',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@Sys.init$COMPUTE_ELEMENT',
    'D;JNE',
    '// goto END_PROGRAM',
    '@Sys.init$END_PROGRAM',
    '0;JMP',
    '// label COMPUTE_ELEMENT',
    '(Sys.init$COMPUTE_ELEMENT)',
    '// push that 0',
    '@0',
    'D = A',
    '@THAT',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// push that 1',
    '@1',
    'D = A',
    '@THAT',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// add',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M + D',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop that 2',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@2',
    'D = A',
    '@THAT',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// push pointer 1',
    '@THAT',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// push constant 1',
    '@1',
    'D = A',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// add',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M + D',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop pointer 1',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@THAT',
    'M = D',
    '// push argument 0',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// push constant 1',
    '@1',
    'D = A',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// sub',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M - D',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop argument 0',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@0',
    'D = A',
    '@ARG',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D',
    '// goto MAIN_LOOP_START',
    '@Sys.init$MAIN_LOOP_START',
    '0;JMP',
    '// label END_PROGRAM',
    '(Sys.init$END_PROGRAM)'
]

snapshots['test_load_vm_commands 1'] = [
    '''VMCommand:
\tcommand: push constant 10
\tcmd_type: PUSH
\tsegment: CONSTANT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: pop local 0
\tcmd_type: POP
\tsegment: LOCAL
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push constant 21
\tcmd_type: PUSH
\tsegment: CONSTANT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push constant 22
\tcmd_type: PUSH
\tsegment: CONSTANT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: pop argument 2
\tcmd_type: POP
\tsegment: ARGUMENT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: pop argument 1
\tcmd_type: POP
\tsegment: ARGUMENT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push constant 36
\tcmd_type: PUSH
\tsegment: CONSTANT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: pop this 6
\tcmd_type: POP
\tsegment: THIS
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push constant 42
\tcmd_type: PUSH
\tsegment: CONSTANT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push constant 45
\tcmd_type: PUSH
\tsegment: CONSTANT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: pop that 5
\tcmd_type: POP
\tsegment: THAT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: pop that 2
\tcmd_type: POP
\tsegment: THAT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push constant 510
\tcmd_type: PUSH
\tsegment: CONSTANT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: pop temp 6
\tcmd_type: POP
\tsegment: TEMP
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push local 0
\tcmd_type: PUSH
\tsegment: LOCAL
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push that 5
\tcmd_type: PUSH
\tsegment: THAT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: add
\tcmd_type: ARITHMETIC
\tsegment: None
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push argument 1
\tcmd_type: PUSH
\tsegment: ARGUMENT
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: sub
\tcmd_type: ARITHMETIC
\tsegment: None
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push this 6
\tcmd_type: PUSH
\tsegment: THIS
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push this 6
\tcmd_type: PUSH
\tsegment: THIS
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: add
\tcmd_type: ARITHMETIC
\tsegment: None
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: sub
\tcmd_type: ARITHMETIC
\tsegment: None
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: push temp 6
\tcmd_type: PUSH
\tsegment: TEMP
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None''',
    '''VMCommand:
\tcommand: add
\tcmd_type: ARITHMETIC
\tsegment: None
\tvm_filename: BasicTest
\tcur_func: Sys.init
\tret_counter: None'''
]

snapshots['test_pop_offset[SegmentType.ARGUMENT-1] 1'] = [
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@1',
    'D = A',
    '@ARG',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D'
]

snapshots['test_pop_offset[SegmentType.LOCAL-42] 1'] = [
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@42',
    'D = A',
    '@LCL',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D'
]

snapshots['test_pop_offset[SegmentType.TEMP-69] 1'] = [
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@69',
    'D = A',
    '@5',
    'AD = D + A',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D'
]

snapshots['test_pop_offset[SegmentType.THAT-69] 1'] = [
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@69',
    'D = A',
    '@THAT',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D'
]

snapshots['test_pop_offset[SegmentType.THIS-9] 1'] = [
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@13',
    'M = D',
    '@9',
    'D = A',
    '@THIS',
    'AD = D + M',
    '@14',
    'M = D',
    '@13',
    'D = M',
    '@14',
    'A = M',
    'M = D'
]

snapshots['test_push_offset[SegmentType.ARGUMENT-1] 1'] = [
    '@1',
    'D = A',
    '@ARG',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_push_offset[SegmentType.LOCAL-42] 1'] = [
    '@42',
    'D = A',
    '@LCL',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_push_offset[SegmentType.TEMP-69] 1'] = [
    '@69',
    'D = A',
    '@5',
    'AD = D + A',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_push_offset[SegmentType.THAT-69] 1'] = [
    '@69',
    'D = A',
    '@THAT',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_push_offset[SegmentType.THIS-9] 1'] = [
    '@9',
    'D = A',
    '@THIS',
    'AD = D + M',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1'
]

snapshots['test_stack_arithmetic[path0] 1'] = [
    '''// push constant 7
''',
    '''@7
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 8
''',
    '''@8
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// add
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M + D
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
'''
]

snapshots['test_stack_arithmetic[path1] 1'] = [
    '''// push constant 17
''',
    '''@17
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 17
''',
    '''@17
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// eq
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.2
''',
    '''D; JEQ
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.2
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.2)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.2)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 17
''',
    '''@17
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 16
''',
    '''@16
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// eq
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.5
''',
    '''D; JEQ
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.5
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.5)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.5)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 16
''',
    '''@16
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 17
''',
    '''@17
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// eq
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.8
''',
    '''D; JEQ
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.8
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.8)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.8)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 892
''',
    '''@892
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 891
''',
    '''@891
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// lt
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.11
''',
    '''D; JLT
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.11
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.11)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.11)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 891
''',
    '''@891
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 892
''',
    '''@892
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// lt
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.14
''',
    '''D; JLT
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.14
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.14)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.14)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 891
''',
    '''@891
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 891
''',
    '''@891
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// lt
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.17
''',
    '''D; JLT
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.17
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.17)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.17)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 32767
''',
    '''@32767
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 32766
''',
    '''@32766
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// gt
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.20
''',
    '''D; JGT
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.20
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.20)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.20)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 32766
''',
    '''@32766
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 32767
''',
    '''@32767
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// gt
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.23
''',
    '''D; JGT
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.23
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.23)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.23)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 32766
''',
    '''@32766
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 32766
''',
    '''@32766
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// gt
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@TRUE_THEN_JUMP.StackTest.26
''',
    '''D; JGT
''',
    '''D = 0
''',
    '''@FALSE_THEN_DONT_JUMP.StackTest.26
''',
    '''0; JMP
''',
    '''(TRUE_THEN_JUMP.StackTest.26)
''',
    '''D = -1
''',
    '''(FALSE_THEN_DONT_JUMP.StackTest.26)
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 57
''',
    '''@57
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 31
''',
    '''@31
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 53
''',
    '''@53
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// add
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M + D
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 112
''',
    '''@112
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// sub
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M - D
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// neg
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''D = - D
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// and
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M & D
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// push constant 82
''',
    '''@82
''',
    '''D = A
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// or
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M | D
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
''',
    '''// not
''',
    '''@SP
''',
    '''M = M - 1
''',
    '''A = M
''',
    '''D = M
''',
    '''D = ! D
''',
    '''@SP
''',
    '''A = M
''',
    '''M = D
''',
    '''@SP
''',
    '''M = M + 1
'''
]

snapshots['test_static 1'] = [
    '// push static 42',
    '@Foo.42',
    'D = M',
    '@SP',
    'A = M',
    'M = D',
    '@SP',
    'M = M + 1',
    '// pop static 69',
    '@SP',
    'M = M - 1',
    'A = M',
    'D = M',
    '@Foo.69',
    'M = D'
]
