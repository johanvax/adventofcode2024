with open('input.txt') as f:
    input = f.readlines()

first = []
second = []

for line in input:
    numbers = line.rsplit(sep = '  ', maxsplit = -1)
    numbers[1] = numbers[1].strip()
    first.append(int(numbers[0]))
    second.append(int(numbers[1]))

first.sort()
second.sort()

sum = 0
for i in range(len(first)):
    sum = sum + abs(first[i] - second[i])

print(sum)
