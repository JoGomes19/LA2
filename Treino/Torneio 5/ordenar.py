import sys


l = []

for s in sys.stdin:
	x = s.split()
	l.append((x[0],len(x[0])))

lAux = sorted(l, key=lambda tup: (tup[1], tup[0]))

for x in lAux:
	print(x[0])

