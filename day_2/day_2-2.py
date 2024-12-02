def is_increasing(numbers):
    for i in range(len(numbers)-1):
        if not (1 <= numbers[i+1] - numbers[i] <= 3):
            return False
    return True

def is_decreasing(numbers):
    for i in range(len(numbers)-1):
        if not (1 <= numbers[i] - numbers[i+1] <= 3):
            return False
    return True

def can_be_safe_by_removal(numbers):
    for i in range(len(numbers)):
        modified = numbers[:i] + numbers[i+1:] # numbers withous numbers[i]
        if is_increasing(modified) or is_decreasing(modified):
            return True
    return False

def is_safe(numbers):
    if is_increasing(numbers) or is_decreasing(numbers):
        return True
    return can_be_safe_by_removal(numbers)

with open('input.txt') as f:
    lines = f.readlines()

safe = 0
for line in lines:
    line = line.strip().split(' ')
    numbers = [int(number) for number in line]
    if is_safe(numbers):
        safe += 1

print(safe)
