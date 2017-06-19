import sys

def media(l):
	return sum(l)/len(l)


m = 0.0
n = 0

for s in sys.stdin:
	l = s.split(",")
	m += media(map(float,l[1:])) # transformar todos os elementos da lista em floats
	n += 1
print ("%2.f" % (m/n))
