# Advent of Code 2021 - day 2

with open("day2.in", "r") as f:
    lines = [x[:-1] for x in list(f.readlines())]

for x in range(len(lines)):
    lines[x] = tuple(lines[x].split())

a, b = 0, 0
for x in range(len(lines)):
    if lines[x][0] == "forward":
        a += int(lines[x][1])
    elif lines[x][0] == "down":
        b += int(lines[x][1])
    elif lines[x][0] == "up":
        b -= int(lines[x][1])

print(f"Part 1 solution is {a * b}")

hori, dep, aim = 0, 0, 0
for x in range(len(lines)):
    if lines[x][0] == "forward":
        hori += int(lines[x][1])
        dep += int(lines[x][1]) * aim
    elif lines[x][0] == "down":
        aim += int(lines[x][1])
    elif lines[x][0] == "up":
        aim -= int(lines[x][1])

print(f"Part 2 solution is {hori * dep}")
