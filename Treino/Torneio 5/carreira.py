import sys

inf = float('inf')

origem,destino = sys.stdin.readline().split()

print origem,destino

adj = {}
for s in sys.stdin:
	x = s.split()
	for i in range(len(x)-2):
		if(i%2 == 0):
			if x[i] not in adj:
				adj[x[i]]   = []
			if x[i+2] not in adj:
				adj[x[i+2]] = []
			adj[x[i]]  += [(x[i+2],int(x[i+1]))]
			adj[x[i+2]]+= [(x[i],int(x[i+1]))]


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



print dijkstra(adj,origem)[destino]


