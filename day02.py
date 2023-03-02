# --- Day 2: 1202 Program Alarm ---
from copy import deepcopy
# Parse input
with open('day02.txt') as f:
    codes_p1 = [int(x) for x in f.read().split(',')]
    codes_p2 = deepcopy(codes_p1)

# Part one

def intcode(intcodes, p1=12, p2=2):
    intcodes[1] = p1
    intcodes[2] = p2
    for n in range(0, len(intcodes), 4):
        number1 = intcodes[intcodes[n+1]]
        number2 = intcodes[intcodes[n+2]]
        position = intcodes[n+3]
        if intcodes[n] == 1:
            intcodes[position] = number1 + number2
        elif intcodes[n] == 2:
            intcodes[position] = number1 * number2
        elif intcodes[n] == 99:
            break

intcode(codes_p1)
print(f"Part one answer: Code at pos 0 --> {codes_p1[0]}")

# Part two
goal = 19690720
for i in range(100):
    for j in range(100):
        codes = deepcopy(codes_p2)
        intcode(codes, i, j)
        if codes[0] == goal:
            result = (100 * i) + j
            print(f"Part two answer: (100 * noun + verb) --> {result}")
            break
