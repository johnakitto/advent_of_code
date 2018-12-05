import time, collections
start_time = time.time()

designs = [design.strip('\n') for design in open('day_03.txt', 'r').readlines()]

squares_covered = {}
for design in designs:
	components = design.split()
	id_number, details = components[0][1:], components[2:4]
	a, b = int(details[0].split(',')[0]), int(details[0].split(',')[1][:-1])
	c, d = int(details[1].split('x')[0]), int(details[1].split('x')[1])
	squares_covered[id_number] = [(x,y) for x in range(a,a+c) for y in range(b,b+d)]

counts = collections.Counter([square for squares in squares_covered.values() for square in squares])

print()
print('part 1 solution: '+ str(len([count for count in counts.values() if count>1])))
print('part 1 runtime: %s sec' % (time.time() - start_time))
print()

start_time = time.time()
winner_found = False
for id_number, squares in squares_covered.items():
	winner_found = True
	for square in squares:
		if counts[square] > 1:
			winner_found = False
			break
	if winner_found:
		print('part 2 solution: '+ id_number)
		print('part 2 runtime: %s sec' % (time.time() - start_time))
		print()
		exit()
