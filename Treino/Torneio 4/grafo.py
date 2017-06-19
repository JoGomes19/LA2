import sys



adj = {}

k = int(sys.stdin.readline()) # numero de cores que quero usar

for l in sys.stdin:
	(o,d) = l.split()
	if o not in adj:
		adj[o] = set()
	if d not in adj:
		adj[d] = set()
	adj[o].add(d)
	adj[d].add(o)

# funcao que testa se um candidado a sulcao e um cadidato valido

def valida(cor): # e uma coloracao valida se para cada nodo, a cor do seu adjacente e diferente
	for o in adj:
		for d in adj:
			if cor[o] == cor[d]:
				return False
	return True


def procura(cor,n):

	if(n == len(adj)):
		return valida(cor)
	for c in range(k):
		v = adj.keys()[n]
		cor[v] = c
		if procura(cor,n+1):
			return True
		cor.pop(v)
	return False
	
cor = {}

print procura(cor,0)



















