import time
start_time = time.time()

with open('day_11.txt', 'r') as file:
	for row in file:
		steps = row.split(',')

x, y = 0, 0
max_steps_away = 0
for step in steps:
	if step == 'ne':
		x += 1
	elif step == 'sw':
		x -= 1
	elif step == 'nw':
		y += 1
	elif step == 'se':
		y -= 1
	elif step == 'n':
		x += 1; y += 1
	elif step == 's':
		x -= 1; y -= 1

	steps_away = min(abs(x),abs(y)) + max(abs(x),abs(y))
	if x != 0 and y != 0 and x/y > 0:
		steps_away = max(abs(x),abs(y))

	if steps_away > max_steps_away:
		max_steps_away = steps_away

print('steps from center: '+ str(steps_away))
print('max steps away during journey: '+ str(max_steps_away))
print('runtime: '+ str(time.time() - start_time) +' sec')
