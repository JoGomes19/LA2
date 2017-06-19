import sys



n = sys.stdin.readline()

l = []
for s in sys.stdin:
	x = s.split()
	l.append(float(x[0]))

pNorte = l[0]
pSul = l[1]
pEste = l[2]
pOeste = l[3]

def geraPonto():
	