# Advent of Code 2021 - day 1

with open("day1.in", "r") as f:
    lines = list(map(int, f.readlines()))

p1 = sum([x0 < x1 for x0, x1 in zip(lines, lines[1:])])
print(f"Part 1 solution is {p1}")

p2 = 0
current, previous = 0, 0
for x in range(0, len(lines) - 3):
    current = lines[x] + lines[x + 1] + lines[x + 2]
    if current > previous:
        p2 += 1
        previous = current
    else:
        previous = current

print(f"Part 2 solution is {p2}")

    

