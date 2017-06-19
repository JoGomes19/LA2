import sys



def soma(l):
	inf = float("inf")
	melhor = atual = 0
	for i in l:
		atual = max(0,atual+i)
		melhor = max(atual,melhor)
	return melhor




l = []
for s in sys.stdin:
	l = s.split()

l = map(int,l)

print soma(l)


