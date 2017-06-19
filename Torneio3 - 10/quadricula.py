import sys
inf = float('inf')

l = []
adj={}

for s in sys.stdin:
	l.append(s)

for x in range(0,len(l)-1): # para remover os \n
	a = l[x]
	l[x] = a[:-1]
o=0
d=1
i=0

for j in range(len(l)-1):
	aux = map(int,l[j].split())
	aux2 = map(int,l[j+1].split())
	#print aux,aux2
	c = len(aux)
	#print c
	for k in range(len(aux)):
		if k == len(aux)-1:
			#print ola
			adj[o] = {(d,aux[k]),(c+1+o,aux[k])}
			o+=1
			#print 'o',o,'d',d
			adj[o] = {(c+1+o,aux[k])}
		else:
			adj[o] = {(d+1,aux[k]),(c+1+o,aux[k])}
		o+=1
		d+=1
aux = map(int,l[j+1].split())
for k in range(len(aux)):
	adj[o] = {(o+1,aux[k])}
	o+=1
	d+=1

adj[o] ={(o,0)}



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

print sorted(dijkstra.keys())
