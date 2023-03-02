# --- Day 3: Crossed Wires ---
import math

# Parse input
with open('day03.txt') as f:
    content = f.readlines()
    cable_1, cable_2 = content[0].strip().split(','),content[1].strip().split(',')

# Part one
points_1, points_2 = set(), set()

def move(start, points, moves, is_set=True):
    x, y = start[0], start[1]
    convert = {'R': 1,'L': -1,'U': 1,'D': -1}
    for move in moves:
        direction = move[0]
        length = int(move[1:])
        delta = convert[direction]
        if direction in ('L', 'R'):
            for _ in range(length):
                x += delta
                if is_set:
                    points.add((x, y))
                else:
                    points.append((x, y))
        elif direction in ('U', 'D'):
            for _ in range(length):
                y += delta
                if is_set:
                    points.add((x, y))
                else:
                    points.append((x, y))   

start = (0,0)
move(start, points_1, cable_1)
move(start, points_2, cable_2)
crosses = points_1 & points_2
min_dist = math.inf
for cross in crosses:
    dist = sum([abs(x) for x in cross])
    if dist < min_dist:
        min_dist = dist
print(f"Part one answer: Closest cross to origin --> {min_dist}")

# Part two
points_1_list, points_2_list = [start], [start]
move(start, points_1_list, cable_1, False)
move(start, points_2_list, cable_2, False)

combined_steps = []
for cross in crosses:
    steps = 0
    for item in points_1_list:
        if item == cross:
            break
        steps += 1
    for item in points_2_list:
        if item == cross:
            break
        steps += 1
    combined_steps.append(steps)
result = min(combined_steps)
print(f"Part two answer: Min amount of combined steps --> {result}")
