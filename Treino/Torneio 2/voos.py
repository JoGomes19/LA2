import sys



def parse(adj):
	for s in sys.stdin:
		o,d = s.split()
		if o not in adj:
			adj[o] = set()
		if d not in adj:
			adj[d] = set()
		adj[o].add(d)
		# se fosse um grafo nao orientado batava por aqui:
		# adj[d].add(o)


origem = sys.stdin.readline().split()[0] # assim garanto que so guardio a informacao necessaria, sem \n por exemplo
adj = {}


def depthFirst(adj,o): # iterativo
	s = [] # uma stack
	visitados = set()
	s.append(o)
	while s: # testa se s nao e vazia
		v = s.pop() # vai a S e tira o ultimo elemento(como se fosse uma stack)
		if v not in visitados:
			visitados.add(v) # marcamos v como visitado
			for w in adj[v]:
				s.append(w) # mete w em S, mas no fim da lista(o mesmo que o push em C)
	return visitados # como usamos um conjunto, nao va devolver na ordem em que descobrimos





parse(adj)

x = depthFirst(adj,origem)

for i in sorted(x):
	print i



	

