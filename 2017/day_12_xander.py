import networkx as nx
import time
start_time = time.time()

graph = nx.Graph()

with open('day_12.txt', 'r') as input:
	for line in input.read().split('\n'):
		node, neighbors = line.split(' <-> ')
		graph.add_edges_from((node, neighbor)
			for neighbor in neighbors.split(', '))

print('Part 1 Solution :', len(nx.node_connected_component(graph, '0')))
print('Part 1 Runtime: ' + str(time.time() - start_time) + ' sec')
start_time = time.time()
print('Part 2 Solution :', nx.number_connected_components(graph))
print('Part 2 Runtime: ' + str(time.time() - start_time) + ' sec')