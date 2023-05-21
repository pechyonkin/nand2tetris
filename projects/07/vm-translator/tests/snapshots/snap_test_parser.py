# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_lead_vm_commands 1"] = [
    "VMCommand('push constant 10', 'PUSH', 'CONSTANT', 'BasicTest.vm')",
    "VMCommand('pop local 0', 'POP', 'LOCAL', 'BasicTest.vm')",
    "VMCommand('push constant 21', 'PUSH', 'CONSTANT', 'BasicTest.vm')",
    "VMCommand('push constant 22', 'PUSH', 'CONSTANT', 'BasicTest.vm')",
    "VMCommand('pop argument 2', 'POP', 'ARGUMENT', 'BasicTest.vm')",
    "VMCommand('pop argument 1', 'POP', 'ARGUMENT', 'BasicTest.vm')",
    "VMCommand('push constant 36', 'PUSH', 'CONSTANT', 'BasicTest.vm')",
    "VMCommand('pop this 6', 'POP', 'THIS', 'BasicTest.vm')",
    "VMCommand('push constant 42', 'PUSH', 'CONSTANT', 'BasicTest.vm')",
    "VMCommand('push constant 45', 'PUSH', 'CONSTANT', 'BasicTest.vm')",
    "VMCommand('pop that 5', 'POP', 'THAT', 'BasicTest.vm')",
    "VMCommand('pop that 2', 'POP', 'THAT', 'BasicTest.vm')",
    "VMCommand('push constant 510', 'PUSH', 'CONSTANT', 'BasicTest.vm')",
    "VMCommand('pop temp 6', 'POP', 'TEMP', 'BasicTest.vm')",
    "VMCommand('push local 0', 'PUSH', 'LOCAL', 'BasicTest.vm')",
    "VMCommand('push that 5', 'PUSH', 'THAT', 'BasicTest.vm')",
    "VMCommand('add', 'ARITHMETIC', 'None', 'BasicTest.vm')",
    "VMCommand('push argument 1', 'PUSH', 'ARGUMENT', 'BasicTest.vm')",
    "VMCommand('sub', 'ARITHMETIC', 'None', 'BasicTest.vm')",
    "VMCommand('push this 6', 'PUSH', 'THIS', 'BasicTest.vm')",
    "VMCommand('push this 6', 'PUSH', 'THIS', 'BasicTest.vm')",
    "VMCommand('add', 'ARITHMETIC', 'None', 'BasicTest.vm')",
    "VMCommand('sub', 'ARITHMETIC', 'None', 'BasicTest.vm')",
    "VMCommand('push temp 6', 'PUSH', 'TEMP', 'BasicTest.vm')",
    "VMCommand('add', 'ARITHMETIC', 'None', 'BasicTest.vm')",
]

snapshots["test_simple_add 1"] = [
    "// push constant 7",
    "@7",
    "D = A",
    "@SP",
    "A = M",
    "M = D",
    "@SP",
    "M = M + 1",
    "// push constant 8",
    "@8",
    "D = A",
    "@SP",
    "A = M",
    "M = D",
    "@SP",
    "M = M + 1",
    "// add",
    "@SP",
    "A = M - 1",
    "D = M",
    "A = A - 1",
    "M = M + D",
    "D = A",
    "@SP",
    "M = D + 1",
]
