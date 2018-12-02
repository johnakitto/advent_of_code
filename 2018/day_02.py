import time, collections
start_time = time.time()

box_ids = [box_id.strip('\n') for box_id in open('day_02.txt', 'r').readlines()]

twice = thrice = 0
for box_id in box_ids:
	counts = collections.Counter(box_id).values()
	twice += 1 if 2 in counts else 0
	thrice += 1 if 3 in counts else 0

print()
print('part 1 solution: %s ' % (twice * thrice))
print('part 1 runtime: %s sec' % (time.time() - start_time))
print()

start_time = time.time()
differs_by_one = lambda str1, str2: True if sum([a!=b for a,b in zip(str1, str2)])==1 else False
for i in range(len(box_ids)-1):
	for j in range(len(box_ids)-1):
		if differs_by_one(box_ids[i], box_ids[j]):
			print('part 2 solution: '+ ''.join(a for a,b in zip(box_ids[i], box_ids[j]) if a==b))
			print('part 2 runtime: %s sec' % (time.time() - start_time))
			print()
			exit()
