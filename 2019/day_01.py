import time
start_time = time.time()

fuel_needed = lambda mass: max((mass//3)-2, 0)
module_masses = [int(mass) for mass in open('day_01.txt', 'r').readlines()]
fuel_masses = [fuel_needed(mass) for mass in module_masses]
total_fuel_mass = sum(fuel_masses)

print()
print('part 1 solution: '+ str(total_fuel_mass))
print('part 1 runtime: %s sec' % (time.time() - start_time))
print()

start_time = time.time()

fuel_still_needed = True
while fuel_still_needed:
	fuel_still_needed = False
	new_fuel_masses = [fuel_needed(mass) for mass in fuel_masses]
	new_fuel_mass = sum(new_fuel_masses)
	if new_fuel_mass > 0:
		fuel_still_needed = True
		total_fuel_mass += new_fuel_mass
		fuel_masses = new_fuel_masses

print('part 2 solution: '+ str(total_fuel_mass))
print('part 2 runtime: %s sec' % (time.time() - start_time))
print()
