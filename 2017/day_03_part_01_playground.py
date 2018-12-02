from math import ceil, sqrt
import time

start_number = lambda layer: 1 + 4*layer*(layer-1) + 1
layer = lambda n: ceil((sqrt(n)-1) / 2)
deviation_from_axis = lambda n, layer: abs((layer-1) - ((n-2) % (2*layer)))

n = int(input('Enter a number: '))
start_time = time.time()

print('steps from center: %s' % (layer(n) + deviation_from_axis(n, layer(n))))
print('total runtime: %s sec' % (time.time() - start_time))

# ------------------------------------------------------------------------------
# Runtime analysis
# ------------------------------------------------------------------------------

from statistics import median
from matplotlib import pyplot as plt

# ------------------------------------------------------------------------------
# Run this block if you want to run the spiral once and plot the results:

# runtimes = []
# steps_from_center = []
# for i in range(2,n+1,ceil(sqrt(n))):
# 	start_time = time.time()
# 	steps_from_center.append(layer(i) + deviation_from_axis(i, layer(i)))
# 	runtimes.append(time.time() - start_time)

# plt.scatter(list(range(2,n+1,ceil(sqrt(n)))), runtimes, s=1, color='k')
# plt.show()

# ------------------------------------------------------------------------------
# Run this block if you want to run it multiple times and take the median
# runtime for each number in the spiral:

runtimes, total_runtimes = [], []
steps_from_center = []
for iterations in range(5):
	for i in range(2,n+1,ceil(sqrt(n))):
		start_time = time.time()
		steps_from_center.append(layer(i) + deviation_from_axis(i, layer(i)))
		runtimes.append(time.time() - start_time)
	total_runtimes.append(list(runtimes))

grouped_runtimes = []
temp_list = []
for i in range(len(total_runtimes[0])):
	for j in range(len(total_runtimes)):
		temp_list.append(total_runtimes[j][i])
	grouped_runtimes.append(list(temp_list))

median_runtimes = []
for runtime in grouped_runtimes:
	median_runtimes.append(median(runtime))

plt.scatter(list(range(2,n+1,ceil(sqrt(n)))), median_runtimes, s=1, color='k')
plt.show()