import sys

inf = float('inf')

#if not(sys.stdin.readlines()): # caso receba nada termina o programa
#	exit();



dimY,dimX = sys.stdin.readline().split()

dimY = int(dimY)
dimX = int(dimX)

if dimY == 0 or dimX == 0:
	exit()

origem = sys.stdin.readline().split()
origem = (int(origem[1]),int(origem[0])) 


l = []
for s in sys.stdin:
	l.append(s)

for x in range(len(l)-1): # para remover os \n
	a = l[x]
	l[x] = a[:-1]

maior = 0
for x in l:
	for i in x:
		if i > maior:
			maior = i

#print type(maior)


maiores = []   # lista com as coordenadas dos pontos mais altos
for la in range(dimY):
	for a in range(dimX):
		if l[a][la] == maior:
			maiores.append((a,la))

adj = {}
for i in range(dimX):
	for j in range(dimY):
		adj[(i,j)] = []

for i in range(dimX):
	for j in range(dimY):
		if (j+1  < dimY):
			adj[(i,j)].append(((i,j+1),abs(ord(l[i][j])-ord(l[i][j+1]))+1))
		if (j-1  >= 0):
			adj[(i,j)].append(((i,j-1),abs(ord(l[i][j])-ord(l[i][j-1]))+1))
		if (i+1  < dimX):
			adj[(i,j)].append(((i+1,j),abs(ord(l[i][j])-ord(l[i+1][j]))+1))
		if (i-1  >= 0):
			adj[(i,j)].append(((i-1,j),abs(ord(l[i][j])-ord(l[i-1][j]))+1))

#######################
## fim - ler o input ##
#######################



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


print adj
dist = dijkstra(adj,origem)

final = []

for x in maiores:
	final.append(dist[x])

print (min(final))






