import sys
import itertools

valor=int(sys.stdin.readline().rstrip())



sequencias=[]
for l in sys.stdin:
	a=l.split()
	a=map(int, a)
	sequencias.append(a)

#print sequencias[0]

for item in sequencias:
	result = [seq for i in xrange(len(item), 0, -1) for seq in itertools.combinations(item, i) if sum(seq) == valor]
	if result!=[]:
		print " ".join(str(x) for x in item)

#result = [seq for i in range(len(sequencias[1]), 0, -1) for seq in itertools.combinations(sequencias[1], i) if sum(seq) == valor]


