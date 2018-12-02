from functools import reduce

with open('day_08.txt', 'r') as file:
	conditions = [line.split('if')[1].strip() for line in file]; file.seek(0)
	swaps = ('inc', '+='), ('dec', '-=')
	actions = [reduce(lambda s, kv: s.replace(*kv), swaps, line.split('if')[0].strip()) for line in file]

variables = list(set([item[0:item.index(' ')] for item in conditions]))
variables = dict(zip(variables, [0]*len(variables)))

current_max = 0
for i in range(len(conditions)):
	end_1, end_2 = conditions[i].index(' '), actions[i].index(' ')
	code_string = 'if variables[conditions[i][0:'+str(end_1)+']]' + conditions[i][end_1:] + ':\n\t'\
						+ 'variables[actions[i][0:'+str(end_2)+']]' + actions[i][end_2:]
	exec(code_string)
	if max(variables.values()) > current_max:
		current_max = max(variables.values())

print('largest variable: ' + max(variables.keys(), key=(lambda key: variables[key])))
print('its value: ' + str(max(variables.values())))
print('largest value ever hit: ' + str(current_max))
