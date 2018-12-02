import time

connections = {}
with open('day_12.txt', 'r') as file:
	for line in file:
		connections[int(line.split()[0])] = [int(number.replace(',', '')) for number in line.split()[2:]]

def recursive_connections(node):
	global connected_to_seed
	for child_node in connections[node]:
		if set(connections[node]).issubset(set(connected_to_seed)):
			connected_to_seed.append(node)
		elif child_node not in connected_to_seed:
			connected_to_seed.append(node)
			recursive_connections(child_node)

seed_node = int(input('what node are you interested in? '))
start_time = time.time()

connected_to_seed = []
recursive_connections(seed_node)

print('nodes connected to '+ str(seed_node) +': '+ str(len(set(connected_to_seed))))
print('part 1 runtime: '+ str(time.time() - start_time) +' sec')

start_time = time.time()
groups = []
for seed_node in connections.keys():
	connected_to_seed = []
	recursive_connections(seed_node)
	connected_to_seed = list(set(connected_to_seed))
	connected_to_seed.sort()
	if connected_to_seed not in groups:
		groups.append(connected_to_seed)

print('unique groups: ' + str(len(groups)))
print('part 2 runtime: ' + str(time.time() - start_time) + ' sec')
