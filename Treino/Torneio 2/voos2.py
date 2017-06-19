import sys

# decobrir o caminho mais curto entre MAD NRT
def parse(adj):
	for s in sys.stdin:
		o,d = s.split()
		if o not in adj:
			adj[o] = set()
		if d not in adj:
			adj[d] = set()
		adj[o].add(d)
		adj[d].add(o)


def breadthFirst(adj,o):
	pais = {}
	visitados = set()
	visitados.add(o)
	q = [] # queue
	q.append(o) # enqueue
	while q:
		c = q.pop(0) # pop(0) retira o elemento da posicao 0
		for n in adj[c]: # c = atual
			if n not in visitados:
				visitados.add(n)
				pais[n] = c # descobrimos n a partir de c
				q.append(n)
	return pais




origem,destino = sys.stdin.readline().split()

adj = {}

parse(adj)
#print adj
path = []

path.append(destino)

pais = breadthFirst(adj,origem)

while destino in pais:
	destino = pais[destino]
	path.insert(0,destino)

for a in path: 
	print a

print len(path)















