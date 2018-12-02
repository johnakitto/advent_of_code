from math import sqrt, ceil

n = int(input('enter a number in the spiral: '))

layer = lambda n: ceil((sqrt(n)-1) / 2)
deviation_from_axis = lambda n, layer: abs((layer-1) - ((n-2) % (2*layer)))

print('steps from center: '+ str(layer(n) + deviation_from_axis(n, layer(n))))
