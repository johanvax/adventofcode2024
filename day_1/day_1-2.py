with open('input.txt') as f:
    input = f.readlines()

first = []
second = []

for line in input:
    numbers = line.rsplit(sep = '  ', maxsplit = -1)
    numbers[1] = numbers[1].strip()
    first.append(int(numbers[0]))
    second.append(int(numbers[1]))

sum = 0
for i in range(len(first)):
    multiplier = 0
    for j in range(len(second)):
        if first[i] == second[j]:
            multiplier = multiplier + 1
    sum = sum + (first[i] * multiplier)

print(sum)
