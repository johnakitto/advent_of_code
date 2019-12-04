import time
start_time = time.time()

og_ints = [int(i) for i in open('day_02.txt', 'r').readline().split(',')]

def run_intcode(ints, noun, verb, errors_dont_matter=False):

	ints[1], ints[2] = noun, verb
	for i in range(0, len(ints), 4):
		if ints[i] == 1:
			ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]]
		elif ints[i] == 2:
			ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]]
		elif ints[i] == 99 or errors_dont_matter:
			break
		else:
			raise Exception('invalid opcode: '+str(ints[i]))

	return ints[0]

print()
print('part 1 solution: '+ str(run_intcode(og_ints.copy(), noun=12, verb=3)))
print('part 1 runtime: %s sec' % (time.time() - start_time))
print()

start_time = time.time()

output, noun, verb = 0, -1, -1
while output != 19690720:
	verb = (verb + 1) % 100
	noun = noun + 1 if verb == 0 else noun
	output = run_intcode(og_ints.copy(), noun, verb, errors_dont_matter=True)

print('part 2 solution: '+ str(100 * noun + verb))
print('part 2 runtime: %s sec' % (time.time() - start_time))
print()
