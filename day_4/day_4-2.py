import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

sum = 0

lines = np.array([list(l.strip()) for l in lines])

for x in range(1, lines.shape[0]-1):
    for y in range(1, lines.shape[1]-1):
        if lines[x][y] != 'A': continue

        if lines[x+1][y+1] == 'S' and lines[x-1][y-1] == 'M' \
            or lines[x+1][y+1] == 'M' and lines[x-1][y-1] == 'S':
            if lines[x+1][y-1] == 'S' and lines[x-1][y+1] == 'M' \
                or lines[x+1][y-1] == 'M' and lines[x-1][y+1] == 'S':
                sum += 1

print(sum)

