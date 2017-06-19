import sys


inf = float('inf')


def parse(adj):
	l = []
	for s in sys.stdin:
		l.append(s)

	for x in range(0,len(l)-1): # para remover os \n
		a = l[x]
		l[x] = a[:-1]
		
	for rua in l:
		if rua[0] not in adj:
			adj[rua[0]] = set()
		if rua[-1] not in adj:
			adj[rua[-1]] = set()
		adj[rua[0]].add((rua[-1],int(len(rua))))
		adj[rua[-1]].add((rua[0],int(len(rua))))
	return adj	

adj = {}
parse(adj)
#print adj

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


tamanho = [] 
final = []
for x in adj:
	tamanho.append(dijkstra(adj,x))
	print dijkstra(adj,x)
#print tamanho
for x in tamanho:
	for i in x:
		final.append(x[i])
#print final

print max(final)


#[{'a': 0, 'c': 14, 'e': 19, 'l': 21, 'o': 4, 's': 9, 'r': 8, 't': 4},
# {'a': 14, 'c': 0, 'e': 15, 'l': 7, 'o': 10, 's': 5, 'r': 14, 't': 18},
# {'a': 19, 'c': 15, 'e': 0, 'l': 9, 'o': 15, 's': 10, 'r': 19, 't': 23}, 
# {'a': 21, 'c': 7, 'e': 9, 'l': 0, 'o': 17, 's': 12, 'r': 21, 't': 25}, 
# {'a': 4, 'c': 10, 'e': 15, 'l': 17, 'o': 0, 's': 5, 'r': 4, 't': 8}, 
# {'a': 9, 'c': 5, 'e': 10, 'l': 12, 'o': 5, 's': 0, 'r': 9, 't': 13}, 
# {'a': 8, 'c': 14, 'e': 19, 'l': 21, 'o': 4, 's': 9, 'r': 0, 't': 12}, 
# {'a': 4, 'c': 18, 'e': 23, 'l': 25, 'o': 8, 's': 13, 'r': 12, 't': 0}]


