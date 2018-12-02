import time
start_time = time.time()

freqs = [int(freq.strip('\n')) for freq in open('day_01.txt', 'r').readlines()]

print()
print('part 1 solution: '+ str(sum(freqs)))
print('part 1 runtime: %s sec' % (time.time() - start_time))
print()

start_time = time.time()
i, result_freq, result_freqs_seen = 0, 0, []
while result_freq not in result_freqs_seen:
	result_freqs_seen.append(result_freq)
	result_freq += freqs[i % len(freqs)]
	i += 1

print('part 2 solution: %s' % result_freq)
print('part 2 runtime: %s sec' % (time.time() - start_time))
print()
