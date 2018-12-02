from functools import reduce
import time
start_time = time.time()

def jumble(circle, lengths):
	global skip_size, current_index
	for length in lengths:
		for step in range(length//2):
			temp = circle[(current_index + (length-1-step)) % len(circle)]
			circle[(current_index + (length-1-step)) % len(circle)] = circle[(current_index+step) % len(circle)]
			circle[(current_index+step) % len(circle)] = temp
		current_index += length + skip_size
		skip_size += 1
	return circle

circle = list(range(256))
lengths = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]

skip_size, current_index = 0, 0
circle = jumble(circle, lengths)

print()
print('multiplication of first 2 list entries: '+ str(circle[0] * circle[1]))
print('part 1 runtime: '+ str(time.time() - start_time) +' sec')
print()

start_time = time.time()
circle = list(range(256))
stringified_lengths = ''.join(str(x) if x==lengths[-1] else str(x)+',' for x in lengths)
ascii_lengths = [ord(i) for i in stringified_lengths] + [17,31,73,47,23]

skip_size, current_index = 0, 0
for iteration in range(64):
	circle = jumble(circle, ascii_lengths)

sparse_hash, dense_hash = circle, []
for block_start in range(0,256,16):
	dense_hash.append(reduce(lambda x,y: x^y, sparse_hash[block_start:block_start+16]))

knot_hash = ''.join(['0x{:02x}'.format(i)[2:] for i in dense_hash])

print('knot hash: '+ knot_hash)
print('part 2 runtime: '+ str(time.time() - start_time) +' sec')
print()
