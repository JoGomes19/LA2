import sys

inf = float('inf')

l = []
l2 = []

for s in sys.stdin:
	x= s.split()
	l.append(list(map(int,x)))


dimH = len(l[0])
dimW = len (l)
destino = (dimW-1,dimH-1)


adj = {}
for i in range(dimW):
	for j in range(dimH):
		adj[(i,j)] = set()

for i in range(dimW):
	for j in range(dimH):
		if (j+1  < dimH):
			adj[(i,j)].add(((i,j+1),abs((l[i][j+1]))))
		if (j-1  >= 0):
			adj[(i,j)].add(((i,j-1),abs((l[i][j-1]))))
		if (i+1  < dimW):
			adj[(i,j)].add(((i+1,j),abs((l[i+1][j]))))
		if (i-1  >= 0):
			adj[(i,j)].add(((i-1,j),abs((l[i-1][j]))))

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
#print adj
origem = (0,0)
dist = dijkstra(adj,origem)
ola = dist[destino]+l[0][0]
print ola

# print adj


# final = []

# for x in destinos:
# 	final.append(dist[x])


# tam = min(final)

# if (tam == inf):
# 	exit()

# print final.index(min(final)),tam