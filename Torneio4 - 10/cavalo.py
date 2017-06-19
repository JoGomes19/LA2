import sys


tab = []
aux = []
for s in sys.stdin:
	x = s.split()
	tab+=x
tab.reverse()

estrelas = []
for x in range(len(tab)):
	for i in range(len(tab[x])):
		if(tab[x][i] == 'F'):
			F = (x,i)
		elif(tab[x][i] == 'I'):
			I = (x,i)
		elif(tab[x][i] == '*'):
			estrelas.append((x,i))
#print F,I
#print estrelas
n = len(tab[0])
adj = {}
for x in range (n):
	for y in range(n):
		adj[(x,y)] = set()


############
## Saltos ##
############

for x in range (n):
	for y in range(n):
		adj[(x,y)]=set()
for (x,y) in adj:
	if (x,y) not in estrelas:
		if(x-1,y-2) in adj and (x-1,y-2) not in estrelas:
			adj[(x,y)].add((x-1,y-2))
			adj[(x-1,y-2)].add((x,y))
		if(x-2,y-1) in adj and (x-2,y-1) not in estrelas:
			adj[(x,y)].add((x-2,y-1))
			adj[(x-2,y-1)].add((x,y))
		if(x-2,y+1) in adj and (x-2,y+1) not in estrelas:
			adj[(x,y)].add((x-2,y+1))
			adj[(x-2,y+1)].add((x,y))
		if(x-1,y+2) in adj and (x-1,y+2) not in estrelas:
			adj[(x,y)].add((x-1,y+2))
			adj[(x-1,y+2)].add((x,y))
		if(x+1,y-2) in adj and (x+1,y-2) not in estrelas:
			adj[(x,y)].add((x+1,y-2))
			adj[(x+1,y-2)].add((x,y))
		if(x+2,y-1) in adj and (x+2,y-1) not in estrelas:
			adj[(x,y)].add((x+2,y-1))
			adj[(x+2,y-1)].add((x,y))
		if(x+2,y+1) in adj and (x+2,y+1) not in estrelas:
			adj[(x,y)].add((x+2,y+1))
			adj[(x+2,y+1)].add((x,y))
		if(x+1,y+2) in adj and (x+1,y+2) not in estrelas:
			adj[(x,y)].add((x+1,y+2))
			adj[(x+1,y+2)].add((x,y))


###############
###############

def bfs(adj,o,d): # descobrir o caminho mais curto entre dois pontos
	novo = o
	t=0
	pais = {}
	visitados = set()
	visitados.add(o)
	q = [] # queue
	q.append(o) # enqueue
	while q:
		c = q.pop(0) # pop(0) retira o elemento da posicao 0
		if (c == d):
			return t
		for n in adj[c]: # c = atual
			#print adj[c]
			if n not in visitados:
				visitados.add(n)
				pais[n] = c # descobrimos n a partir de c
				if(n == novo):
					#print n
					t+=1
					novo = c
				q.append(n)
	return t

print adj


#parent = bfs(adj,I,F) # dicionario com todos os pais e filhos correspondentes
##print parent
#path=[]
#path.append(F) #inicializamos o caminho com o F
#while F in parent:
#	F = parent[F]
#	path.insert(0,F)
print bfs(adj,I,F) 
#if (len(path)-1) == 0:
#	print -1
#else:
#	print len(path)-1










