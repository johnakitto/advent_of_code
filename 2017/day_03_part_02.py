import time, numpy as np

def adjacent_sum(i,j):
	global grid
	grid[i,j] = grid[i,j+1] + grid[i,j-1] + grid[i+1,j] + grid[i+1,j+1] + grid[i+1,j-1] + grid[i-1,j] + grid[i-1,j+1] + grid[i-1,j-1]

def move(step, movement_size):
	global grid, threshold, done
	while step <= movement_size:
		adjacent_sum(i,j)
			if grid[i,j] > threshold:
				done = True
				return
			step += 1

dimension = int(input('how many rows in the numpy array? '))
threshold = int(input('quit after what threshold number? '))

start_time = time.time()
grid = np.zeros(shape=(dimension, dimension))
i = j = (dimension-1)//2
grid[i,j] = 1

done = False
for movement_size in range(1,dimension-2):

	if movement_size % 2 == 1:

		step = 1
		while step <= movement_size:
			j += 1	# move right
			adjacent_sum(i,j)
			if grid[i,j] > threshold:
				done = True
				break
			step += 1
		if done:
			break

		step = 1
		while step <= movement_size:
			i -= 1	# move up
			adjacent_sum(i,j)
			if grid[i,j] > threshold:
				done = True
				break
			step += 1
		if done:
			break

	else:

		step = 1
		while step <= movement_size:
			j -= 1	# move left
			adjacent_sum(i,j)
			if grid[i,j] > threshold:
				done = True
				break
			step += 1
		if done:
			break

		step = 1
		while step <= movement_size:
			i += 1	# move down
			adjacent_sum(i,j)
			if grid[i,j] > threshold:
				done = True
				break
			step += 1
		if done:
			break

print('first number larger than '+ str(threshold) +'-->'+ str(int(grid[i,j])))
print('runtime: '+ str(time.time() - start_time))
