# example.py
# Copyright (c) 2026 mattisva
# Licensed under the MIT License - see the LICENSE file in the project root for details.

# Example program for the simple cell-machine code generator
#
# Operations:
# save(cell, value)  -> assigns a constant value to a cell
# null(cell)         -> sets a cell to 0
# add(a, b, result)  -> result = a + b
# sub(a, b, result)  -> result = a - b

from assembler import main, save, null, add, sub


# Example calculation:
#
# cell7 = 3
# cell5 = 4
# cell1 = 0
# cell1 = cell7 + cell5
# cell6 = 2
# cell0 = 0
# cell0 = cell1 - cell6
#
# Final expected values:
# cell1 = 7
# cell0 = 5

program = (
    save(7, 3) +
    save(5, 4) +
    null(1) +
    add(7, 5, 1) +
    save(6, 2) +
    null(0) +
    sub(1, 6, 0)
)

main(program)