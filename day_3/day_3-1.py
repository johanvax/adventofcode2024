with open('input.txt') as f:
    lines = f.readlines()

sum = 0

for line in lines:
    line = line.split('mul')

    for split in line:
        if split[0] != '(': continue # need the bracket
        closing = split.find(')')
        if closing == -1: continue # need the bracket!!!
        substring = split[1:closing]
        if substring.find(' ') != -1: continue # no spaces allowed
        if substring.find(',') == -1: continue # need the comma
        substring = substring.split(',')
        if len(substring) != 2: continue
        if not (substring[0].isnumeric() and substring[1].isnumeric()): continue
        sum += int(substring[0])*int(substring[1])
print(sum)
