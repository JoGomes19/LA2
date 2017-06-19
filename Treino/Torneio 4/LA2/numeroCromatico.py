import sys



adj = {}



for l in sys.stdin:
	(o,d) = l.split()
	if o not in adj:
		adj[o] = set()
	if d not in adj:
		adj[d] = set()
	adj[o].add(d)
	adj[d].add(o)

# funcao que testa se um candidado a solucao e um cadidato valido

k = len(adj.keys())

def procura(cor,n):

	if(n == len(adj)):
		return True
	for c in range(k):
		v = adj.keys()[n]

		ok = True # para saber se a  cor e valida para o vertice onde estamos, analisando se os seus adjacentes ja tem esta cor C
		for d in adj[v]:
			if d in cor and cor[d] == c:
				ok = False
				break
		if not ok:
			continue # passa ao proximo C

		cor[v] = c
		if procura(cor,n+1):
			return True
		cor.pop(v)
	return False
	
cor = {}

procura(cor,0)


myset = set(cor.values())

print len(myset)







