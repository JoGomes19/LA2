import sys


n = map(int,sys.stdin.readline().split())[0]

l = []
for s in sys.stdin:
	(x,y,z,w) = s.split()
	l.append([int(x),int(y),int(z),int(w)])

adj = {}

for x in l:
	x[0] = (x[0],x[1])
	x[1] = (x[2],x[3])
	del(x[3])
	del(x[2])


############
## Saltos ##
############


for x in range (n):
	for y in range(n):
		adj[(x,y)]=set()
for (x,y) in adj:
	if(x-1,y-2) in adj:
		adj[(x,y)].add((x-1,y-2))
		adj[(x-1,y-2)].add((x,y))
	if(x-2,y-1) in adj:
		adj[(x,y)].add((x-2,y-1))
		adj[(x-2,y-1)].add((x,y))
	if(x-2,y+1) in adj:
		adj[(x,y)].add((x-2,y+1))
		adj[(x-2,y+1)].add((x,y))
	if(x-1,y+2) in adj:
		adj[(x,y)].add((x-1,y+2))
		adj[(x-1,y+2)].add((x,y))
	if(x+1,y-2) in adj:
		adj[(x,y)].add((x+1,y-2))
		adj[(x+1,y-2)].add((x,y))
	if(x+2,y-1) in adj:
		adj[(x,y)].add((x+2,y-1))
		adj[(x+2,y-1)].add((x,y))
	if(x+2,y+1) in adj:
		adj[(x,y)].add((x+2,y+1))
		adj[(x+2,y+1)].add((x,y))
	if(x+1,y+2) in adj:
		adj[(x,y)].add((x+1,y+2))
		adj[(x+1,y+2)].add((x,y))


###############
###############

	

def bfs(adj,o): # descobrir o caminho mais curto entre dois pontos
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



#print l
for x in l:
	origem = x[0]
	destino = x[1]
	
	parent = bfs(adj,origem) # dicionario com todos os pais e filhos correspondentes
	
	path=[]
	path.append(destino) #inicializamos o caminho com o destino
	
	while destino in parent:
		destino = parent[destino]
		path.insert(0,destino)
	
	print path





