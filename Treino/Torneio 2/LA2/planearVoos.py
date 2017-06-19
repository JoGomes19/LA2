import sys

inf = float('inf')

origem,destino = sys.stdin.readline().split()


l = []
adj ={}
for s in sys.stdin:
	o,d,p = s.split()

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

	return dist 
	# devolve os acessiveis atraves da origem, com o preço dessa deslocação a frente
	#{'FRA': 0, 'FAO': 370, 'LON': 200, 'MAD': 500, 'LIS': 300, 'OPO': 300, 'NRT': 1000}


print dijkstra(adj,origem)[destino]






