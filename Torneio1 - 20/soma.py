import sys

def func(x):
	f = 2
	fatores = []
	while(f <= x):
		if x%f == 0:
			fatores.append(f)
			x = x/f
		else:
			f += 1
	return fatores

fatores = []
for s in sys.stdin:
	x = s.split()
	fatores.append(sum(list(set(func(int(x[0]))))))


for x in fatores:
	print x


