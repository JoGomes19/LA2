import sys

# pagar menos entre OPO NRT
# algoritmo de dijkstra

inf = float('inf')

def parse(adj):
	for s in sys.stdin:
		o,d,p = s.split() # origem,destino,peso
		if o not in adj:
			adj[o] = set()
		if d not in adj:
			adj[d] = set()
		adj[o].add((d,int(p)))
		adj[d].add((o,int(p)))

def dijkstra(adj,o):
	orla = []
	pais = {}
	dist = {}
	for v in adj:
		dist[v] = inf
		orla.append(v)
	dist[o] = 0 # dist[o] -> distancia de qq coisa a o
	while orla: #while orla nao vazia
		u = orla[0]
		for w in orla:
			if dist[w] < dist[u]:
				u = w
		orla.remove(u)
		for (v,w) in adj[u]: # v -> visinho de u
			alt = dist[u] + w
			if alt < dist[v]:
				dist[v] = alt
				pais[v] = u

	return pais,dist







origem,destino = sys.stdin.readline().split()

adj = {}

parse(adj)
print adj
pais = {} 
pais,dist = dijkstra(adj,origem)

print dist[destino]





