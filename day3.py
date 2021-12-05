# Advent of Code 2021 - day 3

import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

gamma = []
epsilon = []

for x in range(12):
    gamma.append(0)

for line in lines:
    for index in range(len(line)):
        if line[index] == "1":
            gamma[index] += 1
        else:
            continue

for number in gamma:
    if number > (len(lines) // 2):
        gamma[gamma.index(number)] = 1
        epsilon.append(0)
    else:
        gamma[gamma.index(number)] = 0
        epsilon.append(1)

gamma = "".join(map(str, gamma))
epsilon = "".join(map(str, epsilon))
print(f"Part 1 solution is {int(gamma, 2) * int(epsilon, 2)}")

lines1 = lines.copy()
lines2 = lines.copy()

def count(lines, i):
    count = 0
    for line in lines:
        if line[i] == "1":
            count += 1
        else:
            pass
    if count >= (len(lines) / 2):
        return 1
    else:
        return 0

co2 = "111111111111"
o2 = "000000000000"

def main(inp, lines):
    for i in range(len(inp)):
        if inp[i] == "1":
            control = str(int(not count(lines, i)))
        else:
            control = str(int(count(lines, i)))
        rev_lines = lines.reverse()
        if len(lines) == 1:
            break
        for line in reversed(lines):
            if line[i] == control:
                continue
            else:
                lines.remove(line)

main(o2, lines1)
main(co2, lines2)
o2, co2 = lines1[0], lines2[0]
print(f"Part 2 solution is {int(o2, 2) * int(co2, 2)}")
