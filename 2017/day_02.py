with open('day_02.txt', 'r') as file:
	rows = [row.split('\t') for row in file]
	for i in range(len(rows)):
		for j in range(len(rows[i])):
			rows[i][j] = int(rows[i][j])

checksum_1, checksum_2 = 0, 0
for row in rows:
	checksum_1 += max(row) - min(row)
	done_with_row = False
	for i in range(len(row)):
		for j in range(1,len(row)):
			numer, denom = row[i], row[(i+j) % len(row)]
			if numer % denom == 0 or denom % numer == 0:
				checksum_2 += max(numer // denom, denom // numer)
				done_with_row = True
				break
		if done_with_row:
			break

print('part 1 checksum: '+ str(checksum_1))
print('part 2 checksum: '+ str(checksum_2))
