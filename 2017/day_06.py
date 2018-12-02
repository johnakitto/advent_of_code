banks = '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'
banks = [int(i) for i in banks.split('\t')]

banks_seen = []
cycles = 0
while banks not in banks_seen:
	banks_seen.append(list(banks))
	max_value = blocks_left = max(banks)
	index = banks.index(max_value)
	banks[index] = 0

	while blocks_left > 0:
		banks[(index+1) % len(banks)] += 1
		blocks_left -= 1
		index += 1

	cycles += 1

print('total cycles: ' + str(cycles))
print('cycles in the loop: ' + str(len(banks_seen) - banks_seen.index(banks)))
