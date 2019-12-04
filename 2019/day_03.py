import time
start_time = time.time()

wire_paths = [wire.strip('\n').split(',') for wire in open('day_03.txt', 'r').readlines()]

unit_vectors = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}

def coordinates(wire_path, x=0, y=0, total_steps=0):

	coordinates = {}
	for segment in wire_path:
		letter = segment[0]
		step_size = int(segment[1:])
		for step in range(1, step_size+1):
			coordinates[total_steps+step] = (x+(unit_vectors[letter][0]*step), y+(unit_vectors[letter][1]*step))
		x += unit_vectors[letter][0] * step_size
		y += unit_vectors[letter][1] * step_size
		total_steps += step_size

	return coordinates

wire_one, wire_two = coordinates(wire_paths[0]), coordinates(wire_paths[1])
intersections = set(wire_one.values()).intersection(wire_two.values())
manhattan_distances = [abs(p[0])+abs(p[1]) for p in intersections]

print()
print('part 1 solution: '+ str(min(manhattan_distances)))
print('part 1 runtime: %s sec' % (time.time() - start_time))
print()

start_time = time.time()

total_distances = []
for intersection in intersections:
	total_distance =  min(step for step,coordinate in wire_one.items() if coordinate==intersection)
	total_distance += min(step for step,coordinate in wire_two.items() if coordinate==intersection)
	total_distances.append(total_distance)

print('part 2 solution: '+ str(min(total_distances)))
print('part 2 runtime: %s sec' % (time.time() - start_time))
print()
