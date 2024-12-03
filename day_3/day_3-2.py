with open('input.txt') as f:
    lines = f.readlines()

enabled = True
sum = 0

for line in lines:
    line = line.split('mul')

    for split in line:
        current = enabled
        split = split.strip()
        if enabled:
            if split.find("don't()") != -1: enabled = False
        else:
            if split.find("do()") != -1: enabled = True

        if split[0] != '(': continue # need the bracket
        closing = split.find(')')
        if closing == -1: continue # need the bracket!!!
        substring = split[1:closing]
        if substring.find(' ') != -1: continue # no spaces allowed
        if substring.find(',') == -1: continue # need the comma
        substring2 = substring.split(',')
        if len(substring2) != 2: continue
        if not (substring2[0].isnumeric() and substring2[1].isnumeric()): continue
        if current: sum += int(substring2[0])*int(substring2[1])

print(sum)
