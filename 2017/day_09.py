import re, time
start_time = time.time()

with open('day_09.txt', 'r') as file:
	for line in file:
		stream = line

stream = re.sub('!.', '', stream)
stream_cleaned = re.sub('<[^>]+>', '', stream)
garbage_groups = re.findall('<[^>]+>', stream)

garbage_cleaned = len(stream) - (len(stream_cleaned) + 2*len(garbage_groups))

layer, score = 0, 0
for brace in stream_cleaned:
	if brace == '{':
		layer += 1
	elif brace == '}':
		score += layer
		layer -= 1

print('total score: ' + str(score))
print('garbage cleaned: ' + str(garbage_cleaned))
print('runtime: ' + str(time.time() - start_time) + ' sec')
