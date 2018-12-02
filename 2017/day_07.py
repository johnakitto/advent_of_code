import time
start_time = time.time()

# return the entire row for a given tower name
def row_from_tower_name(tower_name):
	return tower_codes[[tower_codes.index(code) for code in tower_codes if code[0]==tower_name][0]]

# start at the root and recurse your way to the end of the tree, then unravel
def recursive_tower_sum(tower_name):
	global already_printed
	if already_printed:
		return 0
	tower_name_row = row_from_tower_name(tower_name)
	total_weight = tower_name_row[1]

	# if node has children
	if len(tower_name_row) > 2:

		# call the function for all of them
		temp_names, temp_weights = [], []
		for child_name in tower_name_row[2:]:
			child_weight = recursive_tower_sum(child_name)
			temp_names.append(child_name)
			temp_weights.append(child_weight)
			total_weight += child_weight

		# if any set of children don't have the same weights
		if len(list(set(temp_weights))) > 1:
			mode = max(set(temp_weights), key=temp_weights.count)
			layer = dict(zip(temp_names, temp_weights))
			for key in layer.keys():
				if layer[key] != mode:
					odd_ball = key
					difference = mode - layer[key]
					odd_ball_weight = row_from_tower_name(key)[1]
					if not already_printed:
						print(key + ' needs to change by '+ str(difference) +' to become '+ str(odd_ball_weight+difference))
						already_printed = True

	return total_weight

# do some processing on the text file
with open('day_07.txt', 'r') as file:
	tower_codes = [line.split() for line in file]

for i in range(len(tower_codes)):
	tower_codes[i] = [item.strip(',()') for item in tower_codes[i]]
	tower_codes[i][1] = int(tower_codes[i][1])
	try:
		tower_codes[i].remove('->')
	except:
		continue

# the root is the only node that is not a child of another node
all_nodes = [item[0] for item in tower_codes]
children = [item[2:] for item in tower_codes if len(item) > 2]
children = [item for sublist in children for item in sublist]
root = list(set(all_nodes).difference(children))[0]
print('base tower: '+ root)

already_printed = False
recursive_tower_sum(root)

print('runtime: '+ str(time.time() - start_time) +' sec')
