import time, json, collections, datetime as dt
start_time = time.time()

records = [record.strip('\n') for record in open('day_04.txt', 'r').readlines()]

guard_ids, dates = [], []
dates_to_times, dates_to_guards = {}, {}
for record in records:
	if '#' in record:
		guard_id = record.split('#')[1].split()[0]
		start_hour = int(record.split(':')[0][-2:])
		start_minute = int(record.split(':')[1][:2])
		shift_date = record.split()[0][1:].split('-')
		shift_date = dt.date(int(shift_date[0]), int(shift_date[1]), int(shift_date[2]))
		if start_hour==23:
			shift_date += dt.timedelta(days=1)
			start_minute = 0
		guard_ids.append(guard_id)
		dates_to_times[str(shift_date)] = [start_minute]
		dates_to_guards[str(shift_date)] = guard_id

guard_sleep_counts = {guard_id: [0]*60 for guard_id in guard_ids}

for record in records:
	if '#' not in record:
		shift_date = record.split()[0][1:]
		wake_or_sleep_minute = int(record.split(':')[1][:2])
		dates_to_times[shift_date].append(wake_or_sleep_minute)

for date in dates_to_times.keys():
	times = sorted(dates_to_times[date])
	if len(times) > 1:
		minutes_slept = [minute for i in range(1, len(times)-1, 2) for minute in range(times[i], times[i+1])]
		for minute in minutes_slept:
			guard_sleep_counts[dates_to_guards[date]][minute] += 1

print()
[print(('|'+str(i)+' ')*10, end='') for i in range(6)]; print('|  minute tens')
[print('|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 ', end='') for i in range(6)]; print('|  minute ones')
print('|  '*61)

sleepiest_guard = most_total_sleep = sleepiest_guards_sleepiest_minute = 0
consistent_sleeper = most_sleepy_minute = consistent_sleepers_sleepiest_minute = 0
guard_sleep_counts = {int(guard_id): counts for guard_id, counts in guard_sleep_counts.items()}
for guard, sleep_counts in collections.OrderedDict(sorted(guard_sleep_counts.items())).items():
	total_sleep = sum(sleep_counts)
	if total_sleep > most_total_sleep:
		most_total_sleep = total_sleep
		sleepiest_guard = guard
		sleepiest_guards_sleepiest_minute = sleep_counts.index(max(sleep_counts))
	sleepiest_minute = max(sleep_counts)
	if sleepiest_minute > most_sleepy_minute:
		most_sleepy_minute = sleepiest_minute
		consistent_sleeper = guard
		consistent_sleepers_sleepiest_minute = sleep_counts.index(max(sleep_counts))

	for count in sleep_counts:
		if count==0:
			print('|  ', end='')
		elif count!=0 and count>=10:
			print('|'+str(count), end='')
		else:
			print('|'+str(count)+' ', end='')
	print('|  guard '+ str(guard))

print()
print('part 1 solution: '+ str(int(sleepiest_guard) * sleepiest_guards_sleepiest_minute))
print('part 2 solution: '+ str(int(consistent_sleeper) * consistent_sleepers_sleepiest_minute))
print('overall runtime: %s sec' % (time.time() - start_time))
print()



