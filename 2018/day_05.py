import time, re
start_time = time.time()

og_polymer = open('day_05.txt', 'r').readline().strip('\n')

# # recursion fails because you exceed recursion depth
# def reacted_polymer(start_i, polymer):
# 	for i in range(start_i, len(polymer)-1):
# 		if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
# 			return reacted_polymer(max(0, i-1), polymer[:i] + polymer[i+2:])
# 	return polymer

def reacted_polymer(polymer):
	''' fully reacts a polymer and returns final result '''

	start_i = 0
	fully_reacted = False
	while not fully_reacted:
		fully_reacted = True
		for i in range(start_i, len(polymer)-1):
			if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
				fully_reacted = False
				polymer = polymer[:i] + polymer[i+2:]
				start_i = max(0, i-1)
				break

	return polymer

print()
print('part 1 solution: '+ str(len(reacted_polymer(og_polymer))))
print('part 1 runtime: %s sec' % (time.time() - start_time))
print()

start_time = time.time()
shortest_polymer_length = len(og_polymer)
for l in set(og_polymer.upper()):
	test_polymer = re.sub('['+l+chr(ord(l)+32)+']', '', og_polymer)
	test_polymer_length = len(reacted_polymer(test_polymer))
	if test_polymer_length < shortest_polymer_length:
		shortest_polymer_length = test_polymer_length

print()
print('part 2 solution: '+ str(shortest_polymer_length))
print('part 2 runtime: %s sec' % (time.time() - start_time))
print()
