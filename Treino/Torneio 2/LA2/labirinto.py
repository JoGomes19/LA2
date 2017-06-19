import sys


inf = float('inf')
# decobrir o caminho mais curto entre (0,0) (n-1,n-1)

##########################
## inicio - ler o input ##
##########################

n = map(int,sys.stdin.readline().split())[0]
origem = (0,0)
destino = (n-1,n-1)
l = []
adj={}

for s in sys.stdin:
	l.append(s)

for x in range(int(n)):
	for y in range(int(n)):
		if l[x][y] == ' ':
			adj[(x,y)] = set()


			
for (x,y) in adj:
	if (x-1,y) in adj and l[x-1][y] == ' ':
		adj[(x,y)].add((x-1,y))
		adj[(x-1,y)].add((x,y))
	if (x+1,y) in adj and l[x+1][y] == ' ':
		adj[(x,y)].add((x+1,y))
		adj[(x+1,y)].add((x,y))
	if (x,y+1) in adj and l[x][y+1] == ' ':
		adj[(x,y)].add((x,y+1))
		adj[(x,y+1)].add((x,y))
	if(x,y-1) in adj and l[x][y-1] == ' ':
		adj[(x,y)].add((x,y-1))
		adj[(x,y-1)].add((x,y))


#######################
## fim - ler o input ##
#######################



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


parent = bfs(adj,origem) # dicionario com todos os pais e filhos correspondentes(so os que sao == ' ')

path=[]
path.append(destino) #inicializamos o caminho com o destino


while destino in parent:
	destino = parent[destino]
	path.insert(0,destino)

print len(path)-1







