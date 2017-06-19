import sys


def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)



l = []

for s in sys.stdin:
	x = s.split()
	l += (map(int,x))

m = mdc(l[0],l[1])

print m