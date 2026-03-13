# assembler.py
# Copyright (c) 2026 mattisva
# Licensed under the MIT License - see the LICENSE file in the project root for details.

last = 0

def main(inp):
    print(inp + "hlt")

def save(location, data):
    global last
    incs = f"inc {location}\n" * data
    ret = f"""tst {location}
jmp {last + 3}
jmp {last + 5}
dec {location}
jmp {last}
{incs}"""

    last += 5 + data
    return ret


def add(a, b, result):
    global last
    ret = f"""tst {a}
jmp {last + 5}
tst {b}
jmp {last + 8}
jmp {last + 11}
dec {a}
inc {result}
jmp {last}
dec {b}
inc {result}
jmp {last}
"""
    last += 11
    return ret

def null(location):
    global last
    ret = f"""tst {location}
jmp {last +  3}
jmp {last + 5}
dec {location}
jmp {last}
"""
    last += 5
    return ret

def sub(a, b, result):
    global last
    ret = f"""tst {a}
jmp {last + 5}
tst {b}
jmp {last + 8}
jmp {last + 11}
dec {a}
inc {result}
jmp {last}
dec {b}
dec {result}
jmp {last + 2}
"""
    last += 11
    return ret