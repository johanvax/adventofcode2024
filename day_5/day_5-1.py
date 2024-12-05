import math

with open('input.txt') as f:
    lines = f.readlines()

list_lines = [l.strip() for l in lines]
div = list_lines.index('')
rules = list_lines[0:div]
updates = list_lines[div+1:len(list_lines)]

ordering = {}
for rule in rules:
    rule = rule.split('|')
    if int(rule[0]) in ordering:
        ordering.get(int(rule[0])).append(rule[1])
    else:
        ordering[int(rule[0])] = [rule[1]]

sum = 0
for update in updates:
    ok = True
    update = update.split(',')
    previous_values = []
    for i in range(len(update)):
        rule_i = ordering.get(int(update[i]))
        if not rule_i is None:
            for value in rule_i:
                if int(value) in previous_values:
                    ok = False
                    break
        if not ok: break
        previous_values.append(int(update[i]))
        # print(f'i = {i}, value = {update[i]}, rule_i = {rule_i}')

    if ok:
        sum += int(update[math.floor((len(update)-1)/2)])

print(sum)
