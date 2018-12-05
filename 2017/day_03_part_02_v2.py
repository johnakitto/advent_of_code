import time, numpy as np
from math import sqrt, ceil

def move(step_size, i_or_j, plus_or_minus_one, step=1):
	global i, j, n, grid, start_time
	while step <= step_size:
		if i_or_j == 'i':
			i += plus_or_minus_one
		else:
			j += plus_or_minus_one
		grid[i,j] = grid[i,j+1] + grid[i,j-1] + grid[i+1,j] + grid[i+1,j+1] + grid[i+1,j-1] + grid[i-1,j] + grid[i-1,j+1] + grid[i-1,j-1]
		if grid[i,j] > n:
			print('first number larger than '+ str(n) +' = '+ str(int(grid[i,j])))
			print('runtime: %s sec' % (time.time() - start_time))
			print()
			exit()
		step += 1

start_time = time.time()
n = 312051
layer = lambda n: ceil((sqrt(n)-1) / 2)
deviation_from_axis = lambda n, layer: abs((layer-1) - ((n-2) % (2*layer)))

print()
print('steps from center: '+ str(layer(n) + deviation_from_axis(n, layer(n))))
print('runtime %s sec' % (time.time() - start_time))
print()

start_time = time.time()
dimension = 1000
i = j = (dimension-1)//2
grid = np.zeros(shape=(dimension,dimension))
grid[i,j] = 1

for step_size in range(1, dimension-2):
	if step_size % 2 == 1:
		move(step_size, 'j', 1)
		move(step_size, 'i', -1)
	else:
		move(step_size, 'j', -1)
		move(step_size, 'i', 1)
