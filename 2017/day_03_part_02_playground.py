import time
import numpy as np

def adjacent_sum(i,j):
	global grid
	grid[i,j] = grid[i,j+1] + grid[i,j-1] + grid[i+1,j] + grid[i+1,j+1] + grid[i+1,j-1] + grid[i-1,j] + grid[i-1,j+1] + grid[i-1,j-1]

dimension = int(input('How many rows in the numpy array? '))
threshold = int(input('Quit after what threshold number? '))

start_time = time.time()

grid = np.zeros(shape=(dimension, dimension))
i = (dimension-1)//2; j = (dimension-1)//2
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

print('')
print('first number larger than ' + str(threshold) + '-->' + str(int(grid[i,j])))
print('runtime: ' + str(time.time() - start_time))






# -----Playground for Explicit Solution----------------------------

# def chunk(sequence, fours):
# 	sequence.append(3); sequence.append(2)
# 	for j in range(0,fours):
# 		sequence.append(4)

# def sequence_generator(cycles):
# 	sequence = [0,1,2,3,2]
# 	fours = 1
# 	for i in range(cycles):
# 		chunk(sequence, fours); chunk(sequence, fours)
# 		fours += 1
# 	print(sequence)

# sequence_generator(int(input('Enter a number of cycles: ')))

# -----------------------------------------------------------------


