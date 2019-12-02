import time
start_time = time.time()

points = [(int(row.split(',')[0]), int(row.split(', ')[1].strip('\n'))) for row in open('day_06_test.txt').readlines()]

[print(point) for point in points]

# goal: find the size of the largest finite area

# goal 1:
# figure out if a point is on the perimeter and therefore is closest
# to an infinite number of points in that direction

# goal 2:
# given the points that are not closest to an infinite number of points
# figure out how many points they are closest to, printing the largest


