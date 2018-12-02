jump_1, jump_2 = [], []
with open('day_05.txt', 'r') as jump_instructions:
	for line in jump_instructions:
		jump_1.append(int(line))
		jump_2.append(int(line))

i, steps = 0, 0
while i in range(len(jump_1)):
	jump_1[i] += 1; i += jump_1[i]-1
	steps += 1

print('part 1 steps: ' + str(steps))

i, steps = 0, 0
while i in range(len(jump_2)):
	if jump_2[i] >= 3:
		jump_2[i] -= 1; i += jump_2[i]+1
	else:
		jump_2[i] += 1; i += jump_2[i]-1
	steps += 1

print('part 2 steps: ' + str(steps))
