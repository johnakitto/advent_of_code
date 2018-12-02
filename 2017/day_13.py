import time
start_time = time.time()

lengths = {}
with open('day_13.txt', 'r') as file:
	for line in file:
		lengths[int(line.split()[0][:-1])] = int(line.split()[1])

severity = 0
for layer in list(lengths.keys())[1:]:
	if layer % (2*lengths[layer]-2) == 0:
		severity += lengths[layer] * layer

print('severity of first pass: '+ str(severity))
print('part 1 runtime: '+ str(time.time() - start_time) +' sec')

start_time = time.time()
if severity > 0:
	delay = 1
	while severity > 0:
		severity = 0
		for layer in lengths.keys():
			if (layer+delay) % (2*lengths[layer]-2) == 0:
				severity += max(lengths[layer] * layer, 0.1)
				delay += 1
				break

print('delay to pass firewall: '+ str(delay) +' ps')
print('part 2 runtime: '+ str(time.time() - start_time) +' sec')
