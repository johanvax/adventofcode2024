import re
import numpy as np

def count_MAS(line):
    right = [m.start() for m in re.finditer('MAS', line)]
    left = [m.start() for m in re.finditer('SAM', line)]
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

lines = np.array([list(l.strip()) for l in lines])
fdiag, bdiag = get_diagonals(lines)


