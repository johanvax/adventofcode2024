import re
import numpy as np

def count_XMAS(line):
    right = [m.start() for m in re.finditer('XMAS', line)]
    left = [m.start() for m in re.finditer('SAMX', line)]
    return len(right) + len(left)

# Found here: https://stackoverflow.com/a/43311126
def get_diagonals(lines):
    max_row = lines.shape[0]
    max_col = lines.shape[1]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1
    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y].append(lines[y][x])
            bdiag[x-y-min_bdiag].append(lines[y][x])

    return fdiag, bdiag


with open('input_test-1.txt') as f:
    lines = f.readlines()

sum = 0

# horizontal
for line in lines:
    line = line.strip()
    sum += count_XMAS(line)

# vertical (transpose original input)
lines_T = np.array([list(l.strip()) for l in lines]).T
for row in lines_T:
    line = ''.join(list(row))
    sum += count_XMAS(line)

fdiag, bdiag = get_diagonals(lines_T.T)

for row in fdiag:
    line = ''.join(list(row))
    sum += count_XMAS(line)

for row in bdiag:
    line = ''.join(list(row))
    sum += count_XMAS(line)

print(sum)
